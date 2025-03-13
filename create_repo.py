from pathlib import Path

# Создаем структуру данных для тем
topics = [
    {
        "name": "Topic1-ImageGeneration",
        "title": "Генерация изображений с помощью нейросетей",
        "description": "Изучение инструментов для создания изображений с помощью ИИ, таких как Flux, DALL-E 3, Midjourney и Kling.",
        "tools": [
            "[Flux](https://flux.ai/) - Современный инструмент для генерации изображений с высоким качеством.",
            "[DALL-E 3](https://openai.com/dall-e-3/) - Генерация изображений из текста от OpenAI.",
            "[Midjourney](https://www.midjourney.com/) - Художественные стили и креативные визуалы.",
            "[Kling](https://kling.ai/) - Фотореалистичные изображения и видео.",
            "[Glif](https://glif.ai/) - Создание мемов и текстовых вставок."
        ],
        "tutorials": [
            "[Видеоурок по Flux](https://www.youtube.com/watch?v=example-flux) - Пошаговое руководство (замените на актуальную ссылку).",
            "[Руководство по DALL-E 3](https://openai.com/blog/dall-e-3-release/) - Официальная документация.",
            "[Урок по Midjourney](https://www.youtube.com/watch?v=9e8kgoaPZew) - Начало работы с Midjourney."
        ],
        "research": [
            "[Понимание генерации изображений](https://www.analyticsvidhya.com/blog/2022/08/understanding-image-generation-with-ai/) - Обзор технологий.",
            "[GANs для изображений](https://papers.nips.cc/paper/2014/file/5ca3e9b12aa242ef1930322514c55a7b-Paper.pdf) - Ключевой документ по GANs."
        ]
    },
    {
        "name": "Topic2-MusicComposition",
        "title": "Композиция музыки с использованием ИИ",
        "description": "Обзор инструментов для создания музыки с помощью ИИ: Udio, Suno и Mubert.",
        "tools": [
            "[Udio](https://udio.ai/) - Генерация треков из текстовых запросов.",
            "[Suno](https://www.suno.ai/) - Создание песен с вокалом.",
            "[Mubert](https://mubert.com/) - Генерация фоновой музыки."
        ],
        "tutorials": [
            "[Руководство по Udio](https://udio.ai/help) - Начало работы с Udio.",
            "[Гид по Suno](https://help.suno.ai/en/) - Пользовательская документация.",
            "[Введение в Mubert](https://mubert.com/docs) - Основы использования."
        ],
        "research": [
            "[Как ИИ создаёт музыку](https://www.nature.com/articles/d41586-020-01836-7) - Обзор технологий.",
            "[Наука за генерацией музыки](https://www.sciencedaily.com/releases/2020/06/200618144845.htm) - Исследования."
        ]
    },
    {
        "name": "Topic3-VideoProduction",
        "title": "ИИ в видеопроизводстве",
        "description": "Использование ИИ для создания и обработки видео с помощью Sora, Runway, Kling, Wan и Luma AI.",
        "tools": [
            "[Sora](https://openai.com/sora/) - Реалистичные видеосцены от OpenAI.",
            "[Runway](https://runwayml.com/) - Монтаж и эффекты с Gen-3 Alpha.",
            "[Kling](https://kling.ai/) - Генерация видео из текста и изображений.",
            "[Wan](https://www.alibabacloud.com/product/ai) - Бесплатный генератор видео.",
            "[Luma AI](https://lumalabs.ai/) - Быстрая генерация коротких клипов."
        ],
        "tutorials": [
            "[Документация Runway](https://docs.runwayapp.ai/) - Основы использования.",
            "[Введение в Luma AI](https://lumalabs.ai/docs) - Начало работы с Luma."
        ],
        "research": [
            "[Как ИИ меняет видеопроизводство](https://www.forbes.com/sites/forbescommunicationscouncil/2023/04/18/how-ai-is-changing-video-production/) - Обзор.",
            "[Технологии генерации видео](https://www.technologyreview.com/2023/03/16/1070172/ai-video-generation-sora-openai/) - Анализ."
        ]
    },
    {
        "name": "Topic4-TextStorytelling",
        "title": "Нейросети для текста и сторителлинга",
        "description": "Генерация текстов с помощью ChatGPT, Grok и Claude.",
        "tools": [
            "[ChatGPT](https://chat.openai.com/) - Универсальный генератор текста.",
            "[Grok](https://x.ai/grok/) - Креативный ИИ от xAI.",
            "[Claude](https://www.anthropic.com/claude) - Точный и безопасный текстовый ИИ."
        ],
        "tutorials": [
            "[Руководство по ChatGPT](https://help.openai.com/en/articles/6765038-chatgpt-user-guide) - Основы использования.",
            "[Введение в Grok](https://x.ai/docs) - Документация от xAI (предполагаемая ссылка)."
        ],
        "research": [
            "[Понимание генерации текста](https://www.analyticsvidhya.com/blog/2021/09/understanding-ai-text-generation/) - Обзор технологий.",
            "[Основы NLP](https://www.ibm.com/watson/studio/natural-language-generation) - Исследования."
        ]
    },
    {
        "name": "Topic5-DesignArt",
        "title": "Дизайн и искусство с инструментами ИИ",
        "description": "Создание визуалов с помощью Flux, Artbreeder, Leonardo.ai и NightCafe.",
        "tools": [
            "[Flux](https://flux.ai/) - Генерация высококачественных изображений.",
            "[Artbreeder](https://www.artbreeder.com/) - Смешивание стилей и портреты.",
            "[Leonardo.ai](https://leonardo.ai/) - Стилизованные изображения для игр.",
            "[NightCafe](https://nightcafe.studio/) - Креативные эксперименты."
        ],
        "tutorials": [
            "[Урок по Artbreeder](https://www.artbreeder.com/docs) - Основы работы.",
            "[Документация Leonardo.ai](https://docs.leonardo.ai/) - Начало работы."
        ],
        "research": [
            "[ИИ в искусстве](https://www.artofmanliness.com/articles/ai-in-art-and-design/) - Обзор применения.",
            "[Влияние ИИ на креативность](https://www.theguardian.com/technology/2023/mar/23/ai-artificial-intelligence-creative-industries) - Анализ."
        ]
    },
    {
        "name": "Topic6-GamingInteractive",
        "title": "ИИ в играх и интерактивных медиа",
        "description": "Применение ИИ в гейм-дизайне с Flux, Grok, Ludo.ai и Scenario.",
        "tools": [
            "[Flux](https://flux.ai/) - Генерация игровых ассетов.",
            "[Grok](https://x.ai/grok/) - Генерация идей и диалогов для игр.",
            "[Ludo.ai](https://www.ludo.ai/) - Создание концепций игр.",
            "[Scenario](https://www.scenario.com/) - Генерация игровых визуалов."
        ],
        "tutorials": [
            "[Введение в Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Getting-Started.md) - Основы NPC (дополнительно).",
            "[Руководство по процедурной генерации](https://www.raywenderlich.com/2977-procedural-generation-in-games) - Учебник."
        ],
        "research": [
            "[ИИ в играх](https://www.gdcvault.com/gdcmobile/page/47295/AI-in-Games-Past-Present) - Обзор применения.",
            "[Процедурная генерация](https://www.gamedeveloper.com/blogs/procedural-generation-in-games) - Исследования."
        ]
    },
    {
        "name": "Topic7-AIAgents",
        "title": "ИИ-агенты",
        "description": "Изучение автономных ИИ-агентов с Grok, AgentGPT, AutoGen и LangChain.",
        "tools": [
            "[Grok](https://x.ai/grok/) - Разговорный ИИ от xAI.",
            "[AgentGPT](https://agentgpt.reworks.ai/) - Автономные задачи.",
            "[AutoGen](https://www.autogen.ai/) - Многозадачные агенты.",
            "[LangChain](https://python.langchain.com/) - Контекстные агенты."
        ],
        "tutorials": [
            "[Документация AgentGPT](https://agentgpt.reworks.ai/docs) - Основы использования.",
            "[Урок по LangChain](https://python.langchain.com/docs/use_cases/agents) - Руководство по агентам."
        ],
        "research": [
            "[Что такое ИИ-агенты](https://www.techtarget.com/searchstorage/definition/AI-agent) - Определение.",
            "[Построение агентов](https://www.freecodecamp.org/news/building-your-own-ai-agent-with-python-and-openai/) - Практический обзор."
        ]
    },
    {
        "name": "Topic8-SocialMedia",
        "title": "ИИ для контента в социальных сетях",
        "description": "Создание контента для соцсетей с Canva AI, Lumen5, Glif и Opus Clip.",
        "tools": [
            "[Canva AI](https://www.canva.com/ai/) - Дизайн постов.",
            "[Lumen5](https://www.lumen5.com/) - Видео из текста.",
            "[Glif](https://glif.ai/) - Генерация мемов.",
            "[Opus Clip](https://opus.clip/) - Короткие клипы из длинных видео."
        ],
        "tutorials": [
            "[Функции Canva AI](https://www.canva.com/learn/canva-ai/) - Основы работы.",
            "[Руководство по Lumen5](https://www.lumen5.com/blog/lumen5-video-maker-guide) - Учебник."
        ],
        "research": [
            "[Роль ИИ в соцсетях](https://www.forbes.com/sites/forbescommunicationscouncil/2023/05/16/the-role-of-ai-in-social-media/) - Обзор.",
            "[Стратегии с ИИ](https://www.socialmediaexaminer.com/ai-powered-social-media-strategies/) - Анализ."
        ]
    },
    {
        "name": "Topic9-EducationalContent",
        "title": "Создание образовательного контента с ИИ",
        "description": "Использование ИИ для создания уроков с Grok, ChatGPT, Synthesia и Tome.",
        "tools": [
            "[Grok](https://x.ai/grok/) - Генерация идей уроков.",
            "[ChatGPT](https://chat.openai.com/) - Подробные тексты.",
            "[Synthesia](https://www.synthesia.io/) - Видео с аватарами.",
            "[Tome](https://www.tome.app/) - Интерактивные презентации."
        ],
        "tutorials": [
            "[Введение в Synthesia](https://support.synthesia.io/en/articles/4498862-getting-started) - Основы работы.",
            "[Руководство по Tome](https://docs.tome.app/) - Начало работы."
        ],
        "research": [
            "[Будущее образования с ИИ](https://www.brookings.edu/techstream/the-future-of-ai-in-the-classroom/) - Обзор.",
            "[Возможности и вызовы](https://www.un.org/en/academic-impact/ai-international-conference-series-ai-international-conference-series-ai-international-conference-series) - Исследования."
        ]
    },
    {
        "name": "Topic10-Ethics",
        "title": "Этические аспекты применения ИИ в создании контента",
        "description": "Обсуждение этических вопросов ИИ: фейки, авторство, предвзятость с примерами от Flux и Grok.",
        "tools": [
            "[Flux](https://flux.ai/) - Пример генерации изображений.",
            "[Grok](https://x.ai/grok/) - Пример генерации текста.",
            "[Kling](https://kling.ai/) - Пример генерации видео."
        ],
        "tutorials": [
            "[Принципы этики ИИ](https://www.oecd.org/digital/ai-principles.htm) - Рекомендации OECD.",
            "[Рекомендации ЮНЕСКО](https://unesdoc.unesco.org/ark:/48223/pf0000381137) - Обзор этики."
        ],
        "research": [
            "[Этика ИИ-контента](https://www.brookings.edu/techstream/ai-generated-content-and-the-future-of-human-creativity/) - Анализ.",
            "[Проблемы авторства](https://www.theguardian.com/technology/2023/mar/23/ai-artificial-intelligence-copyright-law) - Обзор."
        ]
    }
]

# Создаем корневой README.md с красивым описанием
root_readme = """
# NeuroSchool-Profkom-LETI

![AI Banner](https://via.placeholder.com/800x200.png?text=NeuroSchool+LETI)  
Добро пожаловать в репозиторий **"Нейрошкола от профкома ЛЭТИ"** — образовательного курса, посвящённого применению искусственного интеллекта в создании контента и других областях! Этот репозиторий содержит материалы, ресурсы и ссылки для 10-недельного курса, который стартует 3 марта 2025 года. Здесь вы найдёте всё необходимое для изучения современных ИИ-инструментов и их практического применения.

## О курсе
"Нейрошкола" — это серия лекций и мастер-классов, организованных профкомом ЛЭТИ, чтобы познакомить студентов с возможностями ИИ. Каждая неделя посвящена одной теме, от генерации изображений до этических вопросов. В каждой папке вы найдёте:
- Описание темы.
- Ссылки на инструменты.
- Учебные материалы.
- Научные статьи и исследования.

## Темы курса
1. [Генерация изображений с помощью нейросетей](Topic1-ImageGeneration)  
2. [Композиция музыки с использованием ИИ](Topic2-MusicComposition)  
3. [ИИ в видеопроизводстве](Topic3-VideoProduction)  
4. [Нейросети для текста и сторителлинга](Topic4-TextStorytelling)  
5. [Дизайн и искусство с инструментами ИИ](Topic5-DesignArt)  
6. [ИИ в играх и интерактивных медиа](Topic6-GamingInteractive)  
7. [ИИ-агенты](Topic7-AIAgents)  
8. [ИИ для контента в социальных сетях](Topic8-SocialMedia)  
9. [Создание образовательного контента с ИИ](Topic9-EducationalContent)  
10. [Этические аспекты применения ИИ](Topic10-Ethics)  

## Как использовать
- Перейдите в папку нужной темы.
- Ознакомьтесь с `README.md` для каждой недели.
- Используйте ссылки для изучения инструментов и выполнения домашних заданий.

## Лицензия
Проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE).

## Контакты
Вопросы? Пишите в Telegram-группу курса или на почту профкома ЛЭТИ.

*Создано с помощью ИИ для ИИ-энтузиастов!*
"""

# Создаем лицензию MIT
license_text = """
MIT License

Copyright (c) 2025 Profkom LETI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Создаем папки и файлы
root_dir = Path("NeuroSchool-Profkom-LETI")
root_dir.mkdir(exist_ok=True)

# Записываем корневой README.md
(root_dir / "README.md").write_text(root_readme, encoding="utf-8")

# Записываем LICENSE
(root_dir / "LICENSE").write_text(license_text, encoding="utf-8")

# Создаем папки для каждой темы и их README.md
for topic in topics:
    topic_dir = root_dir / topic["name"]
    topic_dir.mkdir(exist_ok=True)
    
    topic_readme = f"""
# {topic["title"]}

## Описание
{topic["description"]}

## Инструменты
""" + "\n".join(f"- {tool}" for tool in topic["tools"]) + """

## Учебные материалы
""" + "\n".join(f"- {tutorial}" for tutorial in topic["tutorials"]) + """

## Научные работы и исследования
""" + "\n".join(f"- {research}" for research in topic["research"]) + """

## Домашнее задание
См. слайд с ДЗ в презентации для этой недели!
"""
    
    (topic_dir / "README.md").write_text(topic_readme, encoding="utf-8")

print("Структура репозитория успешно создана в папке 'NeuroSchool-Profkom-LETI'!")
