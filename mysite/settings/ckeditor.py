from .base import *

CKEDITOR_BASE_PATH = "ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'extraPlugins': ['codesnippet', 'autogrow', ],
        'codeSnippet_theme': 'docco',
        'autoGrow_onStartup': True,
        'autoGrow_minHeight': '300',
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent',
                'Indent', '-', 'Blockquote', 'CreateDiv'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight',
                'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink'],
            ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks'],
            ['CodeSnippet'],
        ],
    }
}
