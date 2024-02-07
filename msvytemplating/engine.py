import os
import re

from .constants import FOR_LOOP_PATTERN

class MsvyEngine:
    def __init__(self, template_dir="templates"):
        self.template_dir = template_dir

    def render_template(self, template_name, **context):
        template_path = os.path.join(self.template_dir, template_name)

        with open(template_path, "r") as file:
            template_str = file.read()

        return self._render_from_string(template_str, context)

    def _replace_loop(self, match, context):
        inner_var_name = match.group(1)
        list_var_name = match.group(2)
        inner_content = match.group(3)

        iteration_list = context.get(list_var_name, [])
        
        replacement_content = ""
        for item in iteration_list:
            temp_context = { inner_var_name: item }
            item_rendered = self._render_from_string(inner_content, temp_context)
            replacement_content += item_rendered
        
        return replacement_content

    def _render_from_string(self, template_str, context):
        loop_pattern = re.compile(FOR_LOOP_PATTERN, re.DOTALL)
        template_str = loop_pattern.sub(lambda match: self._replace_loop(match, context), template_str)

        for var_name, value in context.items():
            if isinstance(value, list):
                continue

            if isinstance(value, dict):
                for key, val in value.items():
                    nested_placeholder = "{{ $" + var_name + "." + key + " }}"
                    template_str = template_str.replace(nested_placeholder, str(val))
            else:
                placeholder = "{{ $" + var_name + " }}"
                template_str = template_str.replace(placeholder, str(value))
        
        return template_str
