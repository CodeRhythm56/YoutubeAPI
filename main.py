from youtube import YouTube

client_file = 'client-secret.json'
yt = YouTube(client_file)
yt.init_service()

# List channel subscriptions
subscriptions = yt.list_subscriptions()

def listSubscriptions():
  print('Total Subscription: {0}'.format(len(subscriptions)))
  for subscription in subscriptions:
      print('subscription id: {0}'.format(subscription['id']))
      print('channelId id: {0}'.format(subscription['snippet']['resourceId']['channelId']))
      print('channelId title: {0}'.format(subscription['snippet']['title']))
      print('subscribers: {0}'.format(yt.subscribers(str(subscription['snippet']['resourceId']['channelId']))))
      print()
# Unsubscribe channels
def unsubscribeChannels():
  for subscription in subscriptions:
      if(int(yt.subscribers(str(subscription['snippet']['resourceId']['channelId']))) < 7500):
          yt.remove_subscription(subscription['id'])
          print('channel {0} unsubscribed having {1} subs'.format(subscription['snippet']['title'],yt.subscribers(str(subscription['snippet']['resourceId']['channelId']))))
          print('Total Subscription: {0}'.format(len(subscriptions)))

# Subscribe to a channel
def addSubscription(subscriptionID = ""):
  response = yt.add_subscription(subscriptionID)
  print(response)
