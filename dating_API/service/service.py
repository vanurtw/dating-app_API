
def loading_interests_images(instance, file):
    '''Загрузка изображений  интересов'''
    file_exten = file.split('.')
    return f'interests/{instance.slug}.{file_exten}'


