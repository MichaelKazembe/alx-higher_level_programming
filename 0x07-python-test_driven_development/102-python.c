#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_ssize_t i;
	Py_UNICODE *unicode_str;
	char *ascii_str;
	int is_ascii;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	unicode_str = PyUnicode_AsUnicode(p);
	ascii_str = PyUnicode_AsUTF8AndSize(p, &length);
	is_ascii = PyUnicode_IS_ASCII(p);

	printf("  type: compact %s\n", is_ascii ? "ascii" : "unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %s\n", is_ascii ? ascii_str : unicode_str);

	if (!is_ascii)
	{
		printf("  ");
		for (i = 0; i < length; i++)
		{
			printf("%02x ", unicode_str[i]);
		}

	printf("\n");
	}
}
