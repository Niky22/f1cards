from aiogram import types
from aiogram.dispatcher import FSMContext
from Init import dp, bot


@dp.callback_query_handler(text="3090ti LHR", state='*')
async def ti3090LHR(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарты GIGABYTE GeForce RTX 3090 TI GAMING обеспечивают рекордную производительность для геймеров, работая на базе Ampere — архитектуры NVIDIA RTX" \
              " второго поколения. Они оснащены улучшенными ядрами RT и тензорными ядрами, потоковыми мультипроцессорами и высокоскоростной памятью G6X для потрясающих" \
              " игровых возможностей.\n<b>Доходность майнинга в день: </b> 2.00$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3090 ti LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3090 ti LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3090", state='*')
async def LHR3090(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce RTX 3090 GAMING OC разработана для использования в игровых системах. Она использует GIGABYTE WindForce 3X − систему охлаждения," \
              " оснащенную тремя вентиляторами, которые гарантируют высокоэффективное охлаждение платы. Уникальная конфигурация вентиляторов, в которой" \
              " центральный вентилятор поддерживает вращение в альтернативном направлении, снижает турбулентность.Видеочип использует память 24 ГБ GDDR6X и предусматривает" \
              " подключение через интерфейс PCI-E 4.0. В штатном режиме GIGABYTE GeForce RTX 3090 GAMING OC функционирует на частоте 1400 МГц, поддерживая разгон до" \
              " 1755 МГц, что способствует повышению производительности игровой системы.\n<b>Доходность майнинга в день: </b> 1.84$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3090 LHR/1.png'))
    media.attach_photo(types.InputFile('photos/3090 LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3080ti LHR", state='*')
async def ti3080LHR(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GeForce RTX 3080 Ti обеспечивает рекордную производительность для геймеров, работая на базе Ampere — архитектуры NVIDIA RTX второго поколения." \
              " Она оснащена улучшенными ядрами RT и тензорными ядрами, потоковыми мультипроцессорами и высокоскоростной памятью G6X для потрясающих игровых возможностей.\n<b>Доходность майнинга в день: </b> 1.83$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3080 ti LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3080 ti LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3080", state='*')
async def LHR3080(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce RTX 3080 GAMING OC предназначается для модернизации игровой системы. Она использует интерфейс PCI-E 4.0 для подключения к плате." \
              " Использование памяти 12 ГБ GDDR6X с разрядностью 384 бит. Благодаря системе GIGABYTE WindForce 3X, использующей три осевых вентилятора, обеспечивается" \
              " высокоэффективное охлаждение нагревающихся компонентов. Особенность центрального вентилятора в альтернативном вращении, уменьшающем турбулентность соседних" \
              " вентиляторов, повернутых в противоположном направлении. При этом происходит повышение давления воздуха.\n<b>Доходность майнинга в день: </b>1.49$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3080 LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3080 LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3070ti LHR", state='*')
async def ti3070LHR(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce RTX 3070 Ti GAMING OC – игровой видеоадаптер экстра-класса. Устройство оснащено видеопроцессором GeForce RTX 3070 Ti, штатная" \
              " частота которого равна 1575 МГц. Объем памяти значителен – 8 ГБ.Видеокарта GIGABYTE GeForce RTX 3070 Ti GAMING OC обладает высокопроизводительной системой" \
              " охлаждения, представленной тремя осевыми вентиляторами. Предусмотрена возможность остановки вентиляторов. Видеоадаптер, соответственно, может быть" \
              " полностью бесшумным.\n<b>Доходность майнинга в день: </b>1.24$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3070 ti LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3070 ti LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3070 LHR", state='*')
async def LHR3070(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce RTX 3070 GAMING OC (LHR) — это стильное и производительное решение для игровых и рабочих систем. Модель разработана на базе" \
              " архитектуры Ampere с улучшенными тензорными ядрами и мультипроцессорами. Рабочие частоты видеокарты могут варьироваться, что вкупе со скоростной памятью" \
              " GDDR6 объемом 8 ГБ, поддержкой трассировки лучей, а также технологий OpenGL 4.6 и DirectX 12 обеспечит высокую производительность при работе с фото и видео" \
              ", при моделировании, проектировании и запуске игр на высоких настройках изображения. Максимальная температура графического ускорителя может достигать 93°C." \
              " Для охлаждения предусмотрено 3 осевых вентилятора GIGABYTE WindForce 3X.\n<b>Доходность майнинга в день: </b>0.97$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3070 LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3070 LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3060ti LHR", state='*')
async def ti3060LHR(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce RTX 3060 Ti GAMING OC PRO (LHR) станет одним из важнейших элементов мощного игрового компьютера. Система охлаждения WINDFORCE 3X" \
              " в этой модели представлена тремя 80-миллиметровыми вентиляторами и пятью медными тепловыми трубками, имеющими прямой контакт с графическим процессором, для " \
              "наилучшего охлаждения компонентов. Благодаря удлиненной конструкции радиатора обеспечивается лучший отвод тепла.\n<b>Доходность майнинга в день: </b>0.97$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3060 ti LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3060 ti LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3060 LHR", state='*')
async def LHR3060(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce RTX 3060 GAMING OC Rev2.0 способна гарантировать возможность комфортного использования большинства видеоигр. Главный компонент" \
              " видеоадаптера – видеопроцессор GeForce RTX 3060. Устройство не располагает поддержкой мультипроцессорной конфигурации.\n<b>Доходность майнинга в день: </b>0.75$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3060 LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3060 LHR/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="3050 LHR", state='*')
async def LHR3050(call: types.CallbackQuery, state: FSMContext):
    caption = 'Видеокарта GIGABYTE GeForce RTX 3050 GAMING OC — это стильное и производительное решение для игровых и рабочих систем. Модель разработана на базе архитектуры' \
              ' Ampere с улучшенными тензорными ядрами и мультипроцессорами. Рабочие частоты видеокарты могут варьироваться, что вкупе со скоростной памятью GDDR6 объемом' \
              ' 8 ГБ, поддержкой трассировки лучей, а также технологий OpenGL 4.6 и DirectX 12 обеспечит высокую производительность при работе с фото и видео, при' \
              ' моделировании, проектировании и запуске игр на высоких настройках изображения.\n<b>Доходность майнинга в день: </b> 0.40$'
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/3050 LHR/1.jpg'))
    media.attach_photo(types.InputFile('photos/3050 LHR/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="90HX", state='*')
async def HX90(call: types.CallbackQuery, state: FSMContext):
    caption = 'https://aliexpress.ru/item/1005003969269210.html?sku_id=12000027595272636&spm=a2g0o.search.0.2.6d9c356aJfaPH3'
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/90HX/1.png'))
    media.attach_photo(types.InputFile('photos/90HX/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="1660 super", state='*')
async def super1660(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GIGABYTE GeForce GTX 1660 SUPER OC [GV-N166SOC-6GD 1.0], для подключения которой " \
              "используется интерфейс PCI-E 3.0, не имеет поддержки мультипроцессорной конфигурации. Модель " \
              "базируется на широко распространенном графическом процессоре GTX 1660 SUPER. Поддерживаются стандарты " \
              "Vulkan 1.2, OpenGL 4.6 и DirectX 12. Совокупность технических характеристик делает оправданным " \
              "использование устройства в составе игрового компьютера среднего уровня. Вы сможете использовать " \
              "большинство популярных видеоигр.\n<b>Доходность майнинга в день: </b>0.49$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/1660 super/1.png'))
    media.attach_photo(types.InputFile('photos/1660 super/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="1660ti", state='*')
async def ti1660(call: types.CallbackQuery, state: FSMContext):
    caption = "Безупречная надежность, широкая совместимость и высокая производительность – видеокарта ASUS TUF " \
              "Gaming GeForce GTX 1660 Ti EVO OC Edition делает все это доступным в рамках экосистемы устройств серии " \
              "TUF. Устройство оснащается эффективным кулером с двумя вентиляторами, обладающими долговечными " \
              "двойными шарикоподшипниками и сертификацией пыленепроницаемости IP5X.\n<b>Доходность майнинга в день: </b> 0.48$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/1660ti/1.jpg'))
    media.attach_photo(types.InputFile('photos/1660ti/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="2060 super", state='*')
async def super2060(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта GeForce RTX 2060 SUPER создана на базе архитектуры NVIDIA Turing и обеспечивает высочайший " \
              "уровень производительности и графических возможностей для игр и работы с графикой. Зарядите свой ПК " \
              "СУПЕР мощью! \n<b>Доходность майнинга в день: </b>0.65$"
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/2060 super/1.jpg'))
    media.attach_photo(types.InputFile('photos/2060 super/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="6600XT", state='*')
async def XT6600(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта AMD Radeon RX 6600 XT на базе архитектуры AMD RDNA 2, оснащенная 32 мощными улучшенными " \
              "вычислительными блоками, кэш-памятью AMD Infinity Cache и выделенной памятью GDDR6 объемом 8 ГБ, " \
              "обеспечивает сверхвысокую частоту кадров и великолепные ощущения при игре с разрешением 1440p.\n<b>Доходность майнинга в день: </b> 0.52$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/6600XT/1.jpg'))
    media.attach_photo(types.InputFile('photos/6600XT/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="6700XT", state='*')
async def XT6700(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта Sapphire AMD Radeon RX 6700 XT NITRO+ GAMING OC [11306-01-20G] благодаря сочетанию " \
              "производительности и широких возможностей подключения может стать отличным выбором для игровых и " \
              "рабочих станций. Данная модель разработана на базе многоядерного вычислительного блока с поддержкой " \
              "трассировки лучей и использует 12 ГБ скоростной памяти, за счет чего способна обеспечить " \
              "непревзойденный уровень вычислительной мощности для реализации любых ваших творческих и рабочих " \
              "проектов.\n<b>Доходность майнинга в день: </b>0.71$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/6700XT/1.png'))
    media.attach_photo(types.InputFile('photos/6700XT/2.png'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="6800", state='*')
async def a6800(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта Sapphire PULSE AMD Radeon RX 6800 XT Gaming на базе архитектуры AMD RDNA 2, оснащенная 72 " \
              "мощными улучшенными вычислительными блоками, кэш-памятью AMD Infinity Cache объемом 128 МБ и " \
              "выделенной памятью GDDR6 объемом до 16 ГБ, разработана для обеспечения сверхвысокой частоты кадров и " \
              "игрового процесса с разрешением 4K на серьезном уровне.\n<b>Доходность майнинга в день: </b>0.94$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/6800/1.jpg'))
    media.attach_photo(types.InputFile('photos/6800/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="6800XT", state='*')
async def XT6800(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта Sapphire PULSE AMD Radeon RX 6800 XT Gaming на базе архитектуры AMD RDNA 2, оснащенная 72 " \
              "мощными улучшенными вычислительными блоками, кэш-памятью AMD Infinity Cache объемом 128 МБ и " \
              "выделенной памятью GDDR6 объемом до 16 ГБ, разработана для обеспечения сверхвысокой частоты кадров и " \
              "игрового процесса с разрешением 4K на серьезном уровне.\n<b>Доходность майнинга в день: </b> 0.94$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/6800XT/1.jpg'))
    media.attach_photo(types.InputFile('photos/6800XT/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass


@dp.callback_query_handler(text="6900XT", state='*')
async def XT6900(call: types.CallbackQuery, state: FSMContext):
    caption = "Видеокарта Sapphire AMD Radeon RX 6900 XT NITRO+ SE GAMING OC [11308-03-20G], созданная на базе " \
              "архитектуры AMD RDNA 2 с улучшенными характеристиками, обеспечивает высокую частоту кадров для " \
              "достижения плавного игрового процесса в 4K. Номинальная тактовая частота процессора Navi 21 составляет " \
              "2135 МГц и повышается в режиме вычислительного разгона до уровня 2365 МГц. Память стандарта GDDR6 " \
              "имеет объем 16 ГБ и пропускную способность 16 Гбит/с. Из интерфейсов подключения в Sapphire AMD Radeon " \
              "RX 6900 XT NITRO предусмотрены один разъем HDMI и 3 разъема DisplayPort. Система охлаждения Sapphire " \
              "Tri-X с радиатором, медными трубками и 3 осевыми вентиляторами гарантирует эффективный отвод тепла при " \
              "любых вычислительных нагрузках видеокарты. Среди других особенностей отмечаются переключатель BIOS, " \
              "ряд фирменных технологий и многоцветная подсветка RGB.\n<b>Доходность майнинга в день: </b>0.88$ "
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Photos/6900XT/1.jpg'))
    media.attach_photo(types.InputFile('photos/6900XT/2.jpg'), caption=caption)
    await bot.send_media_group(call.message.chat.id, media=media)
    pass