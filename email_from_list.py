# Function to make a user get his email by searching in a list.

email_list = ['6t9u1i2f@qwzou.com', 'x8a3s2q7@mdjbn.net', 'p5r0w4m1@bocnw.org', '9v1d5e6n@jqflh.com', '3o9u4c8e@iwgzl.net', '2d6h9b0t@klqjd.org', '1e4k8s3h@oavbe.com', '0r8f5g9l@tyrcn.net', '7p2o6i1t@uhgxs.org', '5j3z2u1p@brdmq.com', '4x9k2w1f@vnsep.net', '8n1h3j6o@cyflm.org', '6p2w8o4e@rxtfq.com', '5t0s7l3j@kpwhn.net', '9i4a3q0d@gxoyr.org', '3j7u2m9p@hzrld.com', '2e5s1l0d@qywbu.net', '1t4z8u6v@sjgnp.org', '0g8r5b3a@imofe.com', '7v2k9o1n@wyihl.net']

def search_email(email_list, name):
    for email in email_list:
        if name in email:
            return email
    return "Email not found"

print(search_email(email_list,"go"))