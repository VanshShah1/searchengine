import flet as ft
from googlesearch import search

def main(page: ft.Page):

    page.title = "neurum"
    page.window_opacity = 0.7
    page.window_frameless=True
    page.bgcolor=ft.colors.GREY_900
    page.window_height=550
    page.window_resizable=False
    
    links=[]
        
    def submit(event):
        # Use a list comprehension to get all results
        search_results = [result for result in search(prompt.value, num_results=15)]
        
        # Print each result
        for result in search_results:
            links.append(ft.Container(content=ft.Text(result), 
                                      bgcolor=ft.colors.GREY_800,
                                      width=800,
                                      height=40,
                                      border_radius=5,
                                      padding=10)) 
        #t.value=result
        prompt.value=""
        page.update()

    linkscol=ft.Column(controls=links,
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                        spacing=10)

    #t=ft.Text()
    
    prompt=ft.CupertinoTextField(
            placeholder_text="search",
            bgcolor=ft.colors.TRANSPARENT,
            border=ft.border.Border(None),
            height=40,
            on_submit=submit,
           )

    page.add(
        prompt,
        ft.Divider(opacity=0.5),
        linkscol   
    )

ft.app(main)