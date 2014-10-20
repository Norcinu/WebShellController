#define DLLEXPORT extern "C" __declspec(dllexport)

#include <cstdio>

DLLEXPORT void print_msg()
{
    printf("Print Message.\n");
}

