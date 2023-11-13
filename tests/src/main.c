#include "../headers/hello.h"
#include <X11/Xlib.h>

int main()
{
    printTest();
    printf("Hello World");

    Display *display;

    display = XOpenDisplay(NULL);
    if (display == NULL) {
        fprintf(stderr, "Unable to open display\n");
        return 1;
    }

    XCloseDisplay(display);
    return 0;
}