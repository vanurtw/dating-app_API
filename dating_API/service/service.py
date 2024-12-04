
def loading_interests_images(instance, file):
    '''
    Загрузка изображений  интересов
    '''
    file_exten = file.split('.')
    return f'interests/{instance.slug}.{file}'


def loading_profile_images(instance, file):
    '''
    Загрузка изображений профиля аккаунта
    '''
    return f'profiles/{instance.profile}.{file}'