from __future__ import unicode_literals
import unittest
import os
from nayan import python_assertion_evaluator
from nayan.language_registry import _LanguageRegistry, get_registry
from nayan.settings import SERVER_TIMEOUT, code_evaluators


class RegistryTestCase(unittest.TestCase):
    def setUp(self):
        self.registry_object = get_registry()
        self.language_registry = _LanguageRegistry()
        assertion_evaluator_path = ("nayan.python_assertion_evaluator"
            ".PythonAssertionEvaluator"
        )
        stdio_evaluator_path = ("nayan.python_stdio_evaluator."
            "PythonStdIOEvaluator"
        )

        hook_evaluator_path = ("nayan.hook_evaluator."
            "HookEvaluator"
        )
        code_evaluators['python'] = \
        {"standardtestcase": assertion_evaluator_path,
        "stdiobasedtestcase": stdio_evaluator_path,
        "hooktestcase": hook_evaluator_path
        }

    def test_set_register(self):
        evaluator_class = self.registry_object.get_class("python",
            "standardtestcase"
        )
        class_name = getattr(python_assertion_evaluator,
            'PythonAssertionEvaluator'
        )
        self.assertEqual(evaluator_class, class_name)

    def tearDown(self):
        self.registry_object = None

if __name__ == '__main__':
    unittest.main()
