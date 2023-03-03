def parse_emails(email_data, docassemble_response):
    """function to establish email lists based on multiple choice response"""
    package = set()
    for partner in email_data:
        for k, v in partner.items():
            if k in docassemble_response:
                for email in v:
                    package.add(email)
            else:
                continue
    return package