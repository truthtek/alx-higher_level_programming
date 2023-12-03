#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 */ 
void print_python_list_info(PyObject *p) 
{
    PyListObject *list = (PyListObject*)p;
    
    printf("[*] Size of the Python List = %ld\n", PyList_GET_SIZE(list));
    printf("[*] Allocated = %ld\n", list->allocated);
    printf("[*] Python version: %s\n", Py_GetVersion());
}
