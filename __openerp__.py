# -*- coding: utf-8 -*-
{
    'name': 'Document Attachment',
    'version': '0.1',
    'author': 'XCG Consulting',
    'category': 'Document',
    'description': """ enchancements to the ir.attachment module
    to provide admin docs
    """,
    'website': 'http://www.openerp-experts.com',
    'depends': [
        'base',
        'document',
    ],
    'data': [
        'document_attachment.xml',
    ],
    'test': [
    ],
    'installable': True,
}
