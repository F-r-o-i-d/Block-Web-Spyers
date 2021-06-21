blackList = ['https://connect.facebook.net/','https://www.google-analytics.com/analytics.js','https://improving.duckduckgo.com/','https://www.googletagmanager.com/gtm.js','https://www.googletagservices.com/tag/js/gpt.js', 'https://targeting.api.drift.com']
def Formater(text):
    for x in blackList:
        text = text.replace(x, '')
    return text
