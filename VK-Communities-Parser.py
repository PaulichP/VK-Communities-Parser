import requests
import re
import demoji
import time

# Function to get the group ID based on its domain name
def get_group_id(group_domain, access_token):
    base_url = 'https://api.vk.com/method/groups.getById'
    params = {
        'group_id': group_domain,
        'access_token': access_token,
        'v': '5.131'
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    group_id = data['response'][0]['id']
    return group_id

# Function to get posts from a VKontakte group
def get_posts(group_id, access_token, count=100):
    base_url = 'https://api.vk.com/method/wall.get'
    posts = []
    offset = 0
    while count > 0:
        params = {
            'owner_id': -group_id,
            'count': min(count, 100),
            'offset': offset,
            'access_token': access_token,
            'v': '5.131'
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if 'response' in data and 'items' in data['response']:
            items = data['response']['items']
            # Extract the text from posts and add them to the list
            posts.extend([post['text'].replace('\n', ' ') for post in items if post['text']])
            count -= len(items)
            offset += len(items)
        else:
            print('Error occurred while getting posts. Please try adjusting the recommended delay.')
            break

        # Insert a delay between requests to avoid exceeding API limitations
        time.sleep(0)  # Recommended delay in case of errors: 0.35 seconds

    return posts

# Function to save posts to a file
def save_posts_to_file(posts, filename, append=False):
    mode = 'a' if append else 'w'
    with open(filename, mode, encoding='utf-8') as file:
        # Write the posts to the file, separating them with double line breaks
        file.write('\n\n'.join(posts) + '\n\n')

# Function to process the content of a posts file
def process_posts_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove extra line breaks, links, emojis, tags,
    # currency symbols, group mentions, and extra spaces
    content = re.sub(r'\n{2,}', '\n\n', content)
    content = re.sub(r'.*https?://\S+.*\n?', '', content)
    content = re.sub(r'.*vk.me/.*\n?', '', content)
    content = re.sub(r'.*vk.com/.*\n?', '', content)
    content = re.sub(r'.*t.me.*\n?', '', content)
    content = re.sub(r'.*ССЫЛКА В ИСТОЧНИКЕ.*\n?', '', content)
    content = re.sub(r'.*Ссылка в источнике.*\n?', '', content)
    content = re.sub(r'.*cсылка в источнике.*\n?', '', content)
    content = re.sub(r'.*в источнике.*\n?', '', content)
    content = re.sub(r'.*Чекай источник.*\n?', '', content)
    content = re.sub(r'.*чекай источник.*\n?', '', content)
    content = re.sub(r'.*СМОТРИ ИСТОЧНИК.*\n?', '', content)
    content = re.sub(r'.*Жми на источник.*\n?', '', content)
    content = re.sub(r'.*жми на источник.*\n?', '', content)
    content = re.sub(r'.*посмотреть источник.*\n?', '', content)
    content = re.sub(r'.*Посмотреть источник.*\n?', '', content)
    content = re.sub(r'.*Источник снизу.*\n?', '', content)
    content = re.sub(r'.*источник снизу.*\n?', '', content)
    content = re.sub(r'.*Смотри источник.*\n?', '', content)
    content = re.sub(r'.*смотри источник.*\n?', '', content)
    content = re.sub(r'.*в источник.*\n?', '', content)
    content = re.sub(r'.*в ucтoчнuк.*\n?', '', content)
    content = re.sub(r'.*В источнике.*\n?', '', content)
    content = re.sub(r'.*ссылка в комментах.*\n?', '', content)
    content = re.sub(r'.*\(ссылка в источнике\).*\n?', '', content)
    content = re.sub(r'.*\(в источник\).*\n?', '', content)
    content = re.sub(r'.*₽.*\n?', '', content)
    content = re.sub(r'\[club\d+\|[^\]]+\]', '', content)
    content = re.sub(r'\[id\d+\|[^\]]+\]', '', content)
    content = content.replace('\xa0', ' ')
    content = content.replace('\u200B', '')
    content = demoji.replace(content, '')
    content = re.sub(r'\n\n+', '\n\n', content.strip())
    content = re.sub(r' +', ' ', content)

    lines = content.split('\n\n')
    unique_lines = list(set(lines))
    content = '\n\n'.join(unique_lines)

    with open(filename, 'w', encoding='utf-8') as file:
        # Write the processed content back to the file
        file.write(content)

# Set the VKontakte group domain and access token
group_domain = 'group_domain'  # Replace with the actual group ID
access_token = 'access_token'  # Replace with your VKontakte API access token

# Enter the number of posts to process
count = int(input('Enter the number of posts to process: '))

# Set the filename to save the posts
filename = f'{group_domain}.txt'

print(' ')
print('Please wait...\n')

# Get the group ID
group_id = get_group_id(group_domain, access_token)

# Get posts from the group
posts = get_posts(group_id, access_token, count)

# Save the posts to a file
save_posts_to_file(posts, filename)

# Process the posts file
process_posts_file(filename)

# Display information about the saved and processed posts
total_posts = count
valid_posts = len([post for post in posts if post.strip()])

print('Posts saved to file and processed.\n')
print(f'Total processed: {total_posts}')
print(f'After filtering: {valid_posts}')
