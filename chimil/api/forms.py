from django import forms
from django.conf import settings
import requests

class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint ="https://owlbot.info/api/v4/dictionary/{word_id}"
        url = endpoint.format(word_id=word)
        #setting the header value for this url
        headers = {'Authorization': settings.OWLBOT_API}
        #get the api and assign to response
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = "True"
        else:
            result['success'] = "False"
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The OWLBOT API is not available at the moment. Please try again later.'
        return result