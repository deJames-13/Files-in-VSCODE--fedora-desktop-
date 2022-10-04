from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True, name="console")
@stringfilter
def create_script(log):
    console = f"""console.log('{log}');"""
    return console

@register.filter(is_safe=True, name="defaultview")
@stringfilter
def default_view(label):
    print(label)
    DEFAULT_VIEW = f"""
    <div class='container-fluid px-2'>
        <div class='d-flex justify-content-center align-items-center' style='height: 100vh;'>
            <h4>        
                {label}
            </h4>
        </div>
    </div>    
    """
    return DEFAULT_VIEW

