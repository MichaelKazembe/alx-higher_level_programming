#include <Python.h>

void print_python_list_info(PyObject *p) {
    int size = PyList_Size(p);

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

    for (int i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = item->ob_type->tp_name;

        printf("Element %d: %s\n", i, type);
    }
}
