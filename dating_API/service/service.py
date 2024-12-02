
def loading_category_images(instance, file):
    '''Загрузка изображений категорий для интересов'''
    file_exten = file.split('.')
    return f'categories/{instance.slug}.{file_exten}'