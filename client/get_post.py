import markdown
import os
import dearpygui.dearpygui as dpg




def translate_post(foldername): 


    for name in os.listdir(f'{foldername}'):
        if name.endswith('.md'):
            with open(f'main/posts/{foldername}/{name}', 'r') as f:
                content = f.read()
                html_content = markdown.markdown(content)
                with open(f'main/posts_html/{name[:-3]}.html', 'w') as out_f:
                    out_f.write(html_content)




if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title='Bloggy Post Translator', width=400, height=200)

    def translate_callback():
        foldername = dpg.get_value(input_text)
        translate_post(foldername)
        dpg.set_value(output_text, f'Translated posts in folder: {foldername}')

    with dpg.window(label="Post Translator", width=400, height=200):
        dpg.add_text("Enter the folder name containing markdown posts:")
        input_text = dpg.add_input_text(default_value="example_folder")
        dpg.add_button(label="Translate Posts", callback=translate_callback)
        output_text = dpg.add_text("")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()