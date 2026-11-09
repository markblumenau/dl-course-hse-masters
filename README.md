# Глубинное обучение, магистратура НИУ ВШЭ

Курс 2026/27. Преподаватель: Марк Блуменау.

## Материалы

| № | Тема | Лекция | Семинар |
|---|---|---|---|
| 1 | Оптимизация: SGD, momentum, Adam, AdamW | [pdf](lectures/01_Optimization.pdf), [svg](lectures/01_Optimization.svg) | [Введение в PyTorch](seminars/01_Introduction_to_PyTorch.ipynb) |
| 2 | Linear, BatchNorm, Dropout, функции потерь | [pdf](lectures/02_Linear_BatchNorm_Dropout.pdf) | |
| 3 | Свертки | [pdf](lectures/03_Convolution.pdf) | [Свертка изображений](seminars/03_Image_Convolution.ipynb) |
| 4 | Аугментации и основные сверточные архитектуры | [pdf](lectures/04_Augmentations_CNN_Architectures.pdf) | [Классификация изображений](seminars/04_Image_Classification.ipynb) |
| 5 | Детекция и сегментация | [pdf](lectures/05_Detection_Segmentation.pdf) | [Сегментация и детекция](seminars/05_Segmentation_and_Detection.ipynb) |
| 6 | Трекинг, ReID, сегментация | [pdf](lectures/06_Tracking_ReID_Segmentation.pdf), [дополнение: contrastive learning, pose estimation](lectures/06_add_Contrastive_Pose_Estimation.pdf) | [Few-shot и zero-shot learning](seminars/06_Few_Zero_Shot_Learning.ipynb) |
| 7 | Эмбеддинги | [pdf](lectures/07_Embeddings.pdf) | [Word2Vec руками](seminars/07_Word2Vec_by_hand.ipynb), [Word2Vec в gensim](seminars/07_Word2Vec_gensim.ipynb) |

Материалы будут добавляться по ходу курса.

## Домашние задания

| Задание | Тема | Баллы |
|---|---|---:|
| [ДЗ 1](homeworks/HW1/HW1_Light.ipynb) | Полносвязные сети | 10 |
| [Бонус ДЗ 1](homeworks/HW1/HW1_Bonus.ipynb) | Нейросеть на NumPy своими руками | +10 |
| [ДЗ 2](homeworks/HW2/HW2_YOLO.ipynb) | Детекция объектов, YOLO | 10 |
| Бонус ДЗ 2 | mAP и сравнение своего детектора с YOLO11, в конце ДЗ 2 | +1 |
| [ДЗ 3](homeworks/HW3/HW3_Transformers.ipynb) | Трансформеры, суммаризация новостей | 10 |
| Бонус ДЗ 3 | Decoder-only против encoder-decoder, в конце ДЗ 3 | +1 |

Дедлайны и правила сдачи: [homeworks/README.md](homeworks/README.md).

## Оценивание

Пусть $H_1, H_2, H_3$ это оценки за основные части ДЗ с учетом штрафов, $B_1 \leq 10$, $B_2 \leq 1$, $B_3 \leq 1$ это бонусные баллы. Бонусы идут в числитель, но не в знаменатель:

$$
\mathrm{ДЗ} = \frac{H_1 + H_2 + H_3 + B_1 + B_2 + B_3}{3}.
$$

Экзамен оценивается от 0 до 10.

$$
\mathrm{Итог} = \min\left(10,\ 0.6 \cdot \min(12, \mathrm{ДЗ}) + 0.4 \cdot \mathrm{Экз}\right)
$$

Несданное задание дает 0 баллов. Промежуточные величины не округляются, итоговая оценка округляется арифметически.

| Основные ДЗ | Бонусы | ДЗ | Экзамен | Итог |
|---|---:|---:|---:|---:|
| 8, 8, 8 | 0 | 8 | 7 | 7.6 |
| 10, 10, 10 | 6 | 12 | 7 | 10 |
| 10, 10, 0 | 0 | 6.67 | 6 | 6.4 |

## Экзамен

[Билеты](exam/exam_questions.pdf) и [теоретический минимум](exam/theorminimum.pdf).

## Окружение

Нужен Python 3.11 или 3.12. PyTorch и torchvision ставьте по [официальной инструкции](https://pytorch.org/get-started/locally/) под свою ОС и устройство, остальное:

```bash
pip install jupyterlab numpy pandas scipy matplotlib seaborn scikit-learn tqdm
```

Для ДЗ 2 дополнительно нужны `albumentations` и `ultralytics`, для ДЗ 3 `transformers`, `datasets`, `evaluate`, `rouge_score`, `bert_score`. Все задания можно делать в Google Colab или Kaggle.

## Благодарности

Часть материалов и домашних заданий заимствована из других курсов НИУ ВШЭ:
- [Глубинное обучение 1](https://github.com/isadrtdinov/intro-to-dl-hse/tree/master-2024)
- [Основы глубинного обучения](https://github.com/hse-ds/iad-deep-learning)
- [Генеративные модели в машинном обучении](https://github.com/hushchyn-mikhail/gen_models_ai_hse/tree/main)
- [Машинное обучение](https://github.com/esokolov/ml-course-hse/tree/master)
