# RSS-to-intercom
Send articles from your RSS feed over to your intercom account. Your articles will be marked as Drafts, but you can change the code to publish them right away.

You can import the libraries as:
pip install xml.etree.ElementTree as ET
pip install json
pip install requests
  
You can find your Access Token in the Configure > Authentication section in your app within the Developer Hub. You will also see it in your Test & Publish > Your Workspaces page of your app in the Developer Hub. This lists out all of your workspaces that have the app installed.

RSS Feed is the page from where you have to fetch the articles. The articles will be in XML format.

For deleting articles, the FOR loop can be adjusted depending on the number of articles present in your Intercom account. Intercom deletes around 30 articles per call, so here calling the request 5 times will delete about 150 recent articles from my account.
