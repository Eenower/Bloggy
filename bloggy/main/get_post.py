import markdown
import os

def translate_post(foldername): 

    os.makedirs('main/posts_html', exist_ok=True)

    for name in os.listdir(f'main/posts/{foldername}'):
        if name.endswith('.md'):
            with open(f'main/posts/{foldername}/{name}', 'r') as f:
                content = f.read()
                html_content = markdown.markdown(content)
                with open(f'main/posts_html/{name[:-3]}.html', 'w') as out_f:
                    out_f.write(html_content)