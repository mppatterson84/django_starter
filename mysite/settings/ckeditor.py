from .base import *

CKEDITOR_BASE_PATH = "ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
    'default': {
        'contentsCss': [
            os.path.join(STATIC_URL, 'css/base.css'),
            'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css'
        ],
        'skin': 'moono-lisa',
        'removePlugins': ['image'],
        'extraPlugins': ['codesnippet', 'autogrow', 'image2', 'iframe', 'table'],
        'codeSnippet_theme': 'docco',
        'autoGrow_onStartup': True,
        'autoGrow_minHeight': '300',
        'width': '99%',
        'image2_prefillDimensions': False,
        'filebrowserBrowseUrl': '/media/browser/',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source'],
            ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent',
                'Indent', '-', 'Blockquote', 'CreateDiv'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight',
                'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink'],
            ['Image', 'Iframe', 'Table',
                'HorizontalRule', 'Smiley', 'SpecialChar'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks'],
            ['CodeSnippet'],
        ],
    }
}
