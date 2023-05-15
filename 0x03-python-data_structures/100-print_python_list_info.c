#include <Python.h>
/**
 * print_python_list_info - Program prints basic info on python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
	PyObject *item = PyList_GetItem(p, i);
	const char *type = Py_TYPE(item)->tp_name;

	printf("Element %zd: %s\n", i, type);
	}
}
