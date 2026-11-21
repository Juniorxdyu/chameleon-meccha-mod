/* Minimal DLL injector stub for chameleon-meccha-mod */
#include <windows.h>
#include <stdio.h>

int inject(DWORD pid, const char *dll_path) {
    HANDLE hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (!hProc) return 1;

    LPVOID remote = VirtualAllocEx(hProc, NULL, strlen(dll_path) + 1,
                                   MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
    if (!remote) { CloseHandle(hProc); return 2; }

    WriteProcessMemory(hProc, remote, dll_path, strlen(dll_path) + 1, NULL);

    HMODULE k32 = GetModuleHandleA("kernel32.dll");
    LPTHREAD_START_ROUTINE load = (LPTHREAD_START_ROUTINE)GetProcAddress(k32, "LoadLibraryA");
    HANDLE hThread = CreateRemoteThread(hProc, NULL, 0, load, remote, 0, NULL);
    if (!hThread) { CloseHandle(hProc); return 3; }

    WaitForSingleObject(hThread, INFINITE);
    CloseHandle(hThread);
    CloseHandle(hProc);
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 3) { printf("usage: injector <pid> <dll>\n"); return 1; }
    return inject((DWORD)atoi(argv[1]), argv[2]);
}