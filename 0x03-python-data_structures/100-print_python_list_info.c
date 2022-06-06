#include <python.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyObject *obj;

	size = py_size(p);
	alloc = ((pylistObject *)p)->allocated;

	printf("[*] size of the pyhton List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d ", i);

		obj = pylist_GetItem(p, i);
		printf("%s\n", py_TYPE(obj)->tp_name);
	}
}
