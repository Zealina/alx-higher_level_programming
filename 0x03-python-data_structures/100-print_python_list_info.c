#include "object.h"
#include "listobject.h"

/**
 * print_python_list_info - Print information about python objects
 * @p: The python object
 *
 * Return: Nothing, void function
 */
void print_python_list_info(PyObject *p)
{
	unsigned int i;

	printf("[*] Size of the Python List = %d\n", Py_SIZE);
/*	printf("[*] Allocated = %d\n" ...);*/
	
	for (i = 0; i < Py_SIZE; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE);
	}
}
