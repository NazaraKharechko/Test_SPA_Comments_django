from spa.models import PostModel

data_to_insert = [
    {'topic': 'BMW', 'description': 'Bayerische Motoren Werke AG або скор. BMW — німецький автобудівний та '
                                    'авіамоторний концерн і однойменна торгова марка автомобілів преміум- та '
                                    'люкс-класу і мотоциклів. '},
    {'topic': 'Home', 'description': 'Google Home — серія розумних колонок, розроблених компанією Google.  Пристрої '
                                     'дозволяють користувачам давати голосові команди, які виконує Google Assistant, '
                                     'віртуальний асистент корпорації. У систему інтегровані внутрішні та зовнішні '
                                     'сервіси компанії, що дозволяє користувачам слухати музику, відтворювати відео '
                                     'та фото або дізнаватись новини лише за допомогою голосу. Google Home також має '
                                     'інтегровану підтримку автоматизації дому. Перший такий пристрій був випущений у '
                                     'США в листопаді 2016 року та продавався за ціною 129$.'},
    {'topic': 'Work', 'description': 'Workkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'},
]

for data in data_to_insert:
    PostModel.objects.create(**data)

print("Дані додано до бази даних.")
