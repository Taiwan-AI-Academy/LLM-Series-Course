# Copyright 2024 the LlamaFactory team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

LOCALES = {
    "lang": {
        "en": {
            "label": "Lang",
        },
        "ru": {
            "label": "язык",
        },
        "zh": {
            "label": "語言",
        },
        "ko": {
            "label": "언어",
        },
    },
    "model_name": {
        "en": {
            "label": "Model name",
        },
        "ru": {
            "label": "Название модели",
        },
        "zh": {
            "label": "模型名稱",
        },
        "ko": {
            "label": "모델 이름",
        },
    },
    "model_path": {
        "en": {
            "label": "Model path",
            "info": "Path to pretrained model or model identifier from Hugging Face.",
        },
        "ru": {
            "label": "Путь к модели",
            "info": "Путь к предварительно обученной модели или идентификатор модели от Hugging Face.",
        },
        "zh": {
            "label": "模型路徑",
            "info": "本地模型的檔路徑或 Hugging Face 的模型。",
        },
        "ko": {
            "label": "모델 경로",
            "info": "사전 훈련된 모델의 경로 또는 Hugging Face의 모델 식별자.",
        },
    },
    "finetuning_type": {
        "en": {
            "label": "Finetuning method",
        },
        "ru": {
            "label": "Метод дообучения",
        },
        "zh": {
            "label": "微調方法",
        },
        "ko": {
            "label": "파인튜닝 방법",
        },
    },
    "checkpoint_path": {
        "en": {
            "label": "Checkpoint path",
        },
        "ru": {
            "label": "Путь контрольной точки",
        },
        "zh": {
            "label": "檢查點路徑",
        },
        "ko": {
            "label": "체크포인트 경로",
        },
    },
    "advanced_tab": {
        "en": {
            "label": "Advanced configurations",
        },
        "ru": {
            "label": "Расширенные конфигурации",
        },
        "zh": {
            "label": "進階設定",
        },
        "ko": {
            "label": "고급 설정",
        },
    },
    "quantization_bit": {
        "en": {
            "label": "Quantization bit",
            "info": "Enable quantization (QLoRA).",
        },
        "ru": {
            "label": "Уровень квантования",
            "info": "Включить квантование (QLoRA).",
        },
        "zh": {
            "label": "量化等級",
            "info": "啟用量化（QLoRA）。",
        },
        "ko": {
            "label": "양자화 비트",
            "info": "양자화 활성화 (QLoRA).",
        },
    },
    "quantization_method": {
        "en": {
            "label": "Quantization method",
            "info": "Quantization algorithm to use.",
        },
        "ru": {
            "label": "Метод квантования",
            "info": "Алгоритм квантования, который следует использовать.",
        },
        "zh": {
            "label": "量化方法",
            "info": "使用的量化演算法。",
        },
        "ko": {
            "label": "양자화 방법",
            "info": "사용할 양자화 알고리즘.",
        },
    },
    "template": {
        "en": {
            "label": "Prompt template",
            "info": "The template used in constructing prompts.",
        },
        "ru": {
            "label": "Шаблон запроса",
            "info": "Шаблон, используемый при формировании запросов.",
        },
        "zh": {
            "label": "提示模板",
            "info": "建構提示詞時使用的模板",
        },
        "ko": {
            "label": "프롬프트 템플릿",
            "info": "프롬프트 구성에 사용될 템플릿.",
        },
    },
    "rope_scaling": {
        "en": {
            "label": "RoPE scaling",
        },
        "ru": {
            "label": "Масштабирование RoPE",
        },
        "zh": {
            "label": "RoPE 插值方法",
        },
        "ko": {
            "label": "RoPE 스케일링",
        },
    },
    "booster": {
        "en": {
            "label": "Booster",
        },
        "ru": {
            "label": "Ускоритель",
        },
        "zh": {
            "label": "加速方式",
        },
        "ko": {
            "label": "부스터",
        },
    },
    "visual_inputs": {
        "en": {
            "label": "Visual inputs",
        },
        "ru": {
            "label": "визуальные входы",
        },
        "zh": {
            "label": "圖像輸入",
        },
        "ko": {
            "label": "시각적 입력",
        },
    },
    "training_stage": {
        "en": {
            "label": "Stage",
            "info": "The stage to perform in training.",
        },
        "ru": {
            "label": "Этап",
            "info": "Этап выполнения обучения.",
        },
        "zh": {
            "label": "訓練階段",
            "info": "目前採用的訓練方式。",
        },
        "ko": {
            "label": "학습 단계",
            "info": "수행할 학습 방법.",
        },
    },
    "dataset_dir": {
        "en": {
            "label": "Data dir",
            "info": "Path to the data directory.",
        },
        "ru": {
            "label": "Директория данных",
            "info": "Путь к директории данных.",
        },
        "zh": {
            "label": "資料路徑",
            "info": "資料檔案夾的路徑。",
        },
        "ko": {
            "label": "데이터 디렉토리",
            "info": "데이터 디렉토리의 경로.",
        },
    },
    "dataset": {
        "en": {
            "label": "Dataset",
        },
        "ru": {
            "label": "Набор данных",
        },
        "zh": {
            "label": "資料集",
        },
        "ko": {
            "label": "데이터셋",
        },
    },
    "data_preview_btn": {
        "en": {
            "value": "Preview dataset",
        },
        "ru": {
            "value": "Просмотреть набор данных",
        },
        "zh": {
            "value": "預覽資料集",
        },
        "ko": {
            "value": "데이터셋 미리보기",
        },
    },
    "preview_count": {
        "en": {
            "label": "Count",
        },
        "ru": {
            "label": "Количество",
        },
        "zh": {
            "label": "數量",
        },
        "ko": {
            "label": "개수",
        },
    },
    "page_index": {
        "en": {
            "label": "Page",
        },
        "ru": {
            "label": "Страница",
        },
        "zh": {
            "label": "頁數",
        },
        "ko": {
            "label": "페이지",
        },
    },
    "prev_btn": {
        "en": {
            "value": "Prev",
        },
        "ru": {
            "value": "Предыдущая",
        },
        "zh": {
            "value": "上一頁",
        },
        "ko": {
            "value": "이전",
        },
    },
    "next_btn": {
        "en": {
            "value": "Next",
        },
        "ru": {
            "value": "Следующая",
        },
        "zh": {
            "value": "下一頁",
        },
        "ko": {
            "value": "다음",
        },
    },
    "close_btn": {
        "en": {
            "value": "Close",
        },
        "ru": {
            "value": "Закрыть",
        },
        "zh": {
            "value": "關閉",
        },
        "ko": {
            "value": "닫기",
        },
    },
    "preview_samples": {
        "en": {
            "label": "Samples",
        },
        "ru": {
            "label": "Примеры",
        },
        "zh": {
            "label": "樣本",
        },
        "ko": {
            "label": "샘플",
        },
    },
    "learning_rate": {
        "en": {
            "label": "Learning rate",
            "info": "Initial learning rate for AdamW.",
        },
        "ru": {
            "label": "Скорость обучения",
            "info": "Начальная скорость обучения для AdamW.",
        },
        "zh": {
            "label": "學習率",
            "info": "AdamW 優化器的初始學習率。",
        },
        "ko": {
            "label": "학습률",
            "info": "AdamW의 초기 학습률.",
        },

    },
    "num_train_epochs": {
        "en": {
            "label": "Epochs",
            "info": "Total number of training epochs to perform.",
        },
        "ru": {
            "label": "Эпохи",
            "info": "Общее количество эпох обучения.",
        },
        "zh": {
            "label": "訓練輪數",
            "info": "需要執行的訓練總輪數。",
        },
        "ko": {
            "label": "에포크",
            "info": "수행할 총 학습 에포크 수.",
        },
    },
    "max_grad_norm": {
        "en": {
            "label": "Maximum gradient norm",
            "info": "Norm for gradient clipping.",
        },
        "ru": {
            "label": "Максимальная норма градиента",
            "info": "Норма для обрезки градиента.",
        },
        "zh": {
            "label": "最大梯度範數",
            "info": "用於梯度裁剪的範數。",
        },
        "ko": {
            "label": "최대 그레디언트 노름(norm)",
            "info": "그레디언트 클리핑을 위한 노름(norm).",
        },
    },
    "max_samples": {
        "en": {
            "label": "Max samples",
            "info": "Maximum samples per dataset.",
        },
        "ru": {
            "label": "Максимальное количество образцов",
            "info": "Максимальное количество образцов на набор данных.",
        },
        "zh": {
            "label": "最大樣本數",
            "info": "每個資料集的最大樣本數。",
        },
        "ko": {
            "label": "최대 샘플 수",
            "info": "데이터셋 당 최대 샘플 수.",
        },
    },
    "compute_type": {
        "en": {
            "label": "Compute type",
            "info": "Whether to use mixed precision training.",
        },
        "ru": {
            "label": "Тип вычислений",
            "info": "Использовать ли обучение смешанной точности.",
        },
        "zh": {
            "label": "計算類型",
            "info": "是否使用混合精度訓練。",
        },
        "ko": {
            "label": "연산 유형",
            "info": "혼합 정밀도 훈련을 사용할지 여부.",
        },
    },
    "cutoff_len": {
        "en": {
            "label": "Cutoff length",
            "info": "Max tokens in input sequence.",
        },
        "ru": {
            "label": "Длина обрезки",
            "info": "Максимальное количество токенов во входной последовательности.",
        },
        "zh": {
            "label": "截斷長度",
            "info": "輸入序列分詞後的最大長度。",
        },
        "ko": {
            "label": "컷오프 길이",
            "info": "입력 시퀀스의 최대 토큰 수.",
        },
    },
    "batch_size": {
        "en": {
            "label": "Batch size",
            "info": "Number of samples processed on each GPU.",
        },
        "ru": {
            "label": "Размер пакета",
            "info": "Количество образцов для обработки на каждом GPU.",
        },
        "zh": {
            "label": "批次處理大小",
            "info": "每個 GPU 處理的樣本數量。",
        },
        "ko": {
            "label": "배치 크기",
            "info": "각 GPU에서 처리되는 샘플 수.",
        },
    },
    "gradient_accumulation_steps": {
        "en": {
            "label": "Gradient accumulation",
            "info": "Number of steps for gradient accumulation.",
        },
        "ru": {
            "label": "Накопление градиента",
            "info": "Количество шагов накопления градиента.",
        },
        "zh": {
            "label": "梯度累積",
            "info": "梯度累積的步數。",
        },
        "ko": {
            "label": "그레디언트 누적",
            "info": "그레디언트 누적 단계 수.",
        },
    },
    "val_size": {
        "en": {
            "label": "Val size",
            "info": "Proportion of data in the dev set.",
        },
        "ru": {
            "label": "Размер валидации",
            "info": "Пропорция данных в наборе для разработки.",
        },
        "zh": {
            "label": "驗證集比例",
            "info": "驗證集占全部樣本的百分比。",
        },
        "ko": {
            "label": "검증 데이터셋 크기",
            "info": "개발 데이터셋에서 검증 데이터의 비율.",
        },
    },
    "lr_scheduler_type": {
        "en": {
            "label": "LR scheduler",
            "info": "Name of the learning rate scheduler.",
        },
        "ru": {
            "label": "Планировщик скорости обучения",
            "info": "Название планировщика скорости обучения.",
        },
        "zh": {
            "label": "學習率調度器",
            "info": "學習率調度器的名稱。",
        },
        "ko": {
            "label": "LR 스케줄러",
            "info": "학습률 스케줄러의 이름.",
        },
    },
    "extra_tab": {
        "en": {
            "label": "Extra configurations",
        },
        "ru": {
            "label": "Дополнительные конфигурации",
        },
        "zh": {
            "label": "其它參數設定",
        },
        "ko": {
            "label": "추가 구성(configuration)",
        },
    },
    "logging_steps": {
        "en": {
            "label": "Logging steps",
            "info": "Number of steps between two logs.",
        },
        "ru": {
            "label": "Шаги логирования",
            "info": "Количество шагов между двумя записями в журнале.",
        },
        "zh": {
            "label": "日誌間隔",
            "info": "每兩次日誌輸出間的更新步數。",
        },
        "ko": {
            "label": "로깅 스텝",
            "info": "이전 로깅과 다음 로깅 간 스텝 수.",
        },
    },
    "save_steps": {
        "en": {
            "label": "Save steps",
            "info": "Number of steps between two checkpoints.",
        },
        "ru": {
            "label": "Шаги сохранения",
            "info": "Количество шагов между двумя контрольными точками.",
        },
        "zh": {
            "label": "保存間隔",
            "info": "每兩次中斷點保存間的更新步數。",
        },
        "ko": {
            "label": "저장 스텝",
            "info": "이전 체크포인트와 다음 체크포인트 사이의 스텝 수.",
        },
    },
    "warmup_steps": {
        "en": {
            "label": "Warmup steps",
            "info": "Number of steps used for warmup.",
        },
        "ru": {
            "label": "Шаги прогрева",
            "info": "Количество шагов, используемых для прогрева.",
        },
        "zh": {
            "label": " Warmup 步數",
            "info": "學習率 Warmup 採用的步數。",
        },
        "ko": {
            "label": "Warmup 스텝",
            "info": "Warmup에 사용되는 스텝 수.",
        },
    },
    "neftune_alpha": {
        "en": {
            "label": "NEFTune Alpha",
            "info": "Magnitude of noise adding to embedding vectors.",
        },
        "ru": {
            "label": "NEFTune Alpha",
            "info": "Величина шума, добавляемого к векторам вложений.",
        },
        "zh": {
            "label": "NEFTune 雜訊參數",
            "info": "嵌入向量所添加的雜訊大小。",
        },
        "ko": {
            "label": "NEFTune 알파",
            "info": "임베딩 벡터에 추가되는 노이즈의 크기.",
        },
    },
    "optim": {
        "en": {
            "label": "Optimizer",
            "info": "The optimizer to use: adamw_torch, adamw_8bit or adafactor.",
        },
        "ru": {
            "label": "Оптимизатор",
            "info": "Оптимизатор для использования: adamw_torch, adamw_8bit или adafactor.",
        },
        "zh": {
            "label": "優化器",
            "info": "使用的優化器：adamw_torch、adamw_8bit 或 adafactor。",
        },
        "ko": {
            "label": "옵티마이저",
            "info": "사용할 옵티마이저: adamw_torch, adamw_8bit 또는 adafactor 등.",
        },
    },
    "packing": {
        "en": {
            "label": "Pack sequences",
            "info": "Pack sequences into samples of fixed length.",
        },
        "ru": {
            "label": "Упаковка последовательностей",
            "info": "Упаковка последовательностей в образцы фиксированной длины.",
        },
        "zh": {
            "label": "序列打包",
            "info": "將序列打包為等長樣本。",
        },
        "ko": {
            "label": "시퀀스 패킹",
            "info": "고정된 길이의 샘플로 시퀀스를 패킹합니다.",
        },
    },
    "neat_packing": {
        "en": {
            "label": "Use neat packing",
            "info": "Avoid cross-attention between packed sequences.",
        },
        "ru": {
            "label": "Используйте аккуратную упаковку",
            "info": "избегайте перекрестного внимания между упакованными последовательностями.",
        },
        "zh": {
            "label": "使用 neat packing",
            "info": "避免打包後的序列產生交叉注意力。",
        },
        "ko": {
            "label": "니트 패킹 사용",
            "info": "패킹된 시퀀스 간의 크로스 어텐션을 피합니다.",
        },
    },
    "train_on_prompt": {
        "en": {
            "label": "Train on prompt",
            "info": "Disable the label mask on the prompt (only for SFT).",
        },
        "ru": {
            "label": "Тренировка на подсказке",
            "info": "Отключить маску меток на подсказке (только для SFT).",
        },
        "zh": {
            "label": "學習提示詞",
            "info": "不在提示詞的部分添加遮罩（僅適用於 SFT）。",
        },
        "ko": {
            "label": "프롬프트도 학습",
            "info": "프롬프트에서 라벨 마스킹을 비활성화합니다 (SFT에만 해당).",
        },
    },
    "mask_history": {
        "en": {
            "label": "Mask history",
            "info": "Train on the last turn only (only for SFT).",
        },
        "ru": {
            "label": "История масок",
            "info": "Тренироваться только на последнем шаге (только для SFT).",
        },
        "zh": {
            "label": "不學習歷史對話",
            "info": "僅學習最後一輪對話（僅適用於 SFT）。",
        },
        "ko": {
            "label": "히스토리 마스킹",
            "info": "대화 데이터의 마지막 턴만 학습합니다 (SFT에만 해당).",
        },
    },
    "resize_vocab": {
        "en": {
            "label": "Resize token embeddings",
            "info": "Resize the tokenizer vocab and the embedding layers.",
        },
        "ru": {
            "label": "Изменение размера токенных эмбеддингов",
            "info": "Изменить размер словаря токенизатора и слоев эмбеддинга.",
        },
        "zh": {
            "label": "更改詞表大小",
            "info": "更改分詞器詞表和嵌入層的大小。",
        },
        "ko": {
            "label": "토큰 임베딩의 사이즈 조정",
            "info": "토크나이저 어휘와 임베딩 레이어의 크기를 조정합니다.",
        },
    },
    "use_llama_pro": {
        "en": {
            "label": "Enable LLaMA Pro",
            "info": "Make the parameters in the expanded blocks trainable.",
        },
        "ru": {
            "label": "Включить LLaMA Pro",
            "info": "Сделать параметры в расширенных блоках обучаемыми.",
        },
        "zh": {
            "label": "使用 LLaMA Pro",
            "info": "僅訓練塊擴展後的參數。",
        },
        "ko": {
            "label": "LLaMA Pro 사용",
            "info": "확장된 블록의 매개변수를 학습 가능하게 만듭니다.",
        },
    },
    "shift_attn": {
        "en": {
            "label": "Enable S^2 Attention",
            "info": "Use shift short attention proposed by LongLoRA.",
        },
        "ru": {
            "label": "Включить S^2 внимание",
            "info": "Использовать сдвиг внимания на короткие дистанции предложенный LongLoRA.",
        },
        "zh": {
            "label": "使用 S^2 Attention",
            "info": "使用 LongLoRA 提出的 shift short attention。",
        },
        "ko": {
            "label": "S^2 Attention 사용",
            "info": "LongLoRA에서 제안한 shift short attention을 사용합니다.",
        },
    },
    "report_to": {
        "en": {
            "label": "Enable external logger",
            "info": "Use TensorBoard or wandb to log experiment.",
        },
        "ru": {
            "label": "Включить внешний регистратор",
            "info": "Использовать TensorBoard или wandb для ведения журнала экспериментов.",
        },
        "zh": {
            "label": "啟用外部記錄",
            "info": "使用 TensorBoard 或 wandb 記錄實驗。",
        },
        "ko": {
            "label": "외부 logger 활성화",
            "info": "TensorBoard 또는 wandb를 사용하여 실험을 기록합니다.",
        },
    },
    "freeze_tab": {
        "en": {
            "label": "Freeze tuning configurations",
        },
        "ru": {
            "label": "конфигурации для настройки заморозки",
        },
        "zh": {
            "label": "部分參數微調設定",
        },
        "ko": {
            "label": "Freeze tuning 설정",
        },
    },
    "freeze_trainable_layers": {
        "en": {
            "label": "Trainable layers",
            "info": "Number of the last(+)/first(-) hidden layers to be set as trainable.",
        },
        "ru": {
            "label": "Обучаемые слои",
            "info": "Количество последних (+)/первых (-) скрытых слоев, которые будут установлены как обучаемые.",
        },
        "zh": {
            "label": "可訓練層數",
            "info": "最末尾（+）/最前端（-）可訓練隱藏層的數量。",
        },
        "ko": {
            "label": "학습 가능한 레이어",
            "info": "학습 가능하게 설정할 마지막(+)/처음(-) 히든 레이어의 수.",
        },
    },
    "freeze_trainable_modules": {
        "en": {
            "label": "Trainable modules",
            "info": "Name(s) of trainable modules. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Обучаемые модули",
            "info": "Название обучаемых модулей. Используйте запятые для разделения нескольких модулей.",
        },
        "zh": {
            "label": "可訓練模組",
            "info": "可訓練模組的名稱。使用英文逗號分隔多個名稱。",
        },
        "ko": {
            "label": "학습 가능한 모듈",
            "info": "학습 가능한 모듈의 이름. 여러 모듈을 구분하려면 쉼표(,)를 사용하세요.",
        },
    },
    "freeze_extra_modules": {
        "en": {
            "label": "Extra modules (optional)",
            "info": (
                "Name(s) of modules apart from hidden layers to be set as trainable. "
                "Use commas to separate multiple modules."
            ),
        },
        "ru": {
            "label": "Дополнительные модули (опционально)",
            "info": (
                "Имена модулей, кроме скрытых слоев, которые следует установить в качестве обучаемых. "
                "Используйте запятые для разделения нескольких модулей."
            ),
        },
        "zh": {
            "label": "額外模組（非必填）",
            "info": "除隱藏層以外的可訓練模組名稱。使用英文逗號分隔多個名稱。",
        },
        "ko": {
            "label": "추가 모듈 (선택 사항)",
            "info": "학습 가능한 모듈의 이름(히든 레이어 제외). 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
    },
    "lora_tab": {
        "en": {
            "label": "LoRA configurations",
        },
        "ru": {
            "label": "Конфигурации LoRA",
        },
        "zh": {
            "label": "LoRA 參數設定",
        },
        "ko": {
            "label": "LoRA 구성",
        },
    },
    "lora_rank": {
        "en": {
            "label": "LoRA rank",
            "info": "The rank of LoRA matrices.",
        },
        "ru": {
            "label": "Ранг матриц LoRA",
            "info": "Ранг матриц LoRA.",
        },
        "zh": {
            "label": "LoRA 秩",
            "info": "LoRA 矩陣的秩大小。",
        },
        "ko": {
            "label": "LoRA 랭크",
            "info": "LoRA 행렬의 랭크.",
        },
    },
    "lora_alpha": {
        "en": {
            "label": "LoRA alpha",
            "info": "Lora scaling coefficient.",
        },
        "ru": {
            "label": "LoRA alpha",
            "info": "Коэффициент масштабирования LoRA.",
        },
        "zh": {
            "label": "LoRA 縮放係數",
            "info": "LoRA 縮放係數大小。",
        },
        "ko": {
            "label": "LoRA 알파",
            "info": "LoRA 스케일링 계수.",
        },
    },
    "lora_dropout": {
        "en": {
            "label": "LoRA dropout",
            "info": "Dropout ratio of LoRA weights.",
        },
        "ru": {
            "label": "Вероятность отсева LoRA",
            "info": "Вероятность отсева весов LoRA.",
        },
        "zh": {
            "label": "LoRA 隨機丟棄",
            "info": "LoRA 權重隨機丟棄的概率。",
        },
        "ko": {
            "label": "LoRA 드롭아웃",
            "info": "LoRA 가중치의 드롭아웃 비율.",
        },
    },
    "loraplus_lr_ratio": {
        "en": {
            "label": "LoRA+ LR ratio",
            "info": "The LR ratio of the B matrices in LoRA.",
        },
        "ru": {
            "label": "LoRA+ LR коэффициент",
            "info": "Коэффициент LR матриц B в LoRA.",
        },
        "zh": {
            "label": "LoRA+ 學習率比例",
            "info": "LoRA+ 中 B 矩陣的學習率倍數。",
        },
        "ko": {
            "label": "LoRA+ LR 비율",
            "info": "LoRA에서 B 행렬의 LR 비율.",
        },
    },
    "create_new_adapter": {
        "en": {
            "label": "Create new adapter",
            "info": "Create a new adapter with randomly initialized weight upon the existing one.",
        },
        "ru": {
            "label": "Создать новый адаптер",
            "info": "Создать новый адаптер с случайной инициализацией веса на основе существующего.",
        },
        "zh": {
            "label": "新建adapter",
            "info": "在現有的adapter上創建一個隨機初始化後的新adapter。",
        },
        "ko": {
            "label": "새 어댑터 생성",
            "info": "기존 어댑터 위에 무작위로 초기화된 가중치를 가진 새 어댑터를 생성합니다.",
        },
    },
    "use_rslora": {
        "en": {
            "label": "Use rslora",
            "info": "Use the rank stabilization scaling factor for LoRA layer.",
        },
        "ru": {
            "label": "Использовать rslora",
            "info": "Использовать коэффициент масштабирования стабилизации ранга для слоя LoRA.",
        },
        "zh": {
            "label": "使用 rslora",
            "info": "對 LoRA 層使用秩穩定縮放方法。",
        },
        "ko": {
            "label": "rslora 사용",
            "info": "LoRA 레이어에 랭크 안정화 스케일링 계수를 사용합니다.",
        },
    },
    "use_dora": {
        "en": {
            "label": "Use DoRA",
            "info": "Use weight-decomposed LoRA.",
        },
        "ru": {
            "label": "Используйте DoRA",
            "info": "Используйте LoRA с декомпозицией весов.",
        },
        "zh": {
            "label": "使用 DoRA",
            "info": "使用權重分解的 LoRA。",
        },
        "ko": {
            "label": "DoRA 사용",
            "info": "가중치-분해 LoRA를 사용합니다.",
        },
    },
    "use_pissa": {
        "en": {
            "label": "Use PiSSA",
            "info": "Use PiSSA method.",
        },
        "ru": {
            "label": "используйте PiSSA",
            "info": "Используйте метод PiSSA.",
        },
        "zh": {
            "label": "使用 PiSSA",
            "info": "使用 PiSSA 方法。",
        },
        "ko": {
            "label": "PiSSA 사용",
            "info": "PiSSA 방법을 사용합니다.",
        },
    },
    "lora_target": {
        "en": {
            "label": "LoRA modules (optional)",
            "info": "Name(s) of modules to apply LoRA. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Модули LoRA (опционально)",
            "info": "Имена модулей для применения LoRA. Используйте запятые для разделения нескольких модулей.",
        },
        "zh": {
            "label": "LoRA 作用模組（非必填）",
            "info": "應用 LoRA 的模組名稱。使用英文逗號分隔多個名稱。",
        },
        "ko": {
            "label": "LoRA 모듈 (선택 사항)",
            "info": "LoRA를 적용할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
    },
    "additional_target": {
        "en": {
            "label": "Additional modules (optional)",
            "info": (
                "Name(s) of modules apart from LoRA layers to be set as trainable. "
                "Use commas to separate multiple modules."
            ),
        },
        "ru": {
            "label": "Дополнительные модули (опционально)",
            "info": (
                "Имена модулей, кроме слоев LoRA, которые следует установить в качестве обучаемых. "
                "Используйте запятые для разделения нескольких модулей."
            ),
        },
        "zh": {
            "label": "附加模組（非必填）",
            "info": "除 LoRA 層以外的可訓練模組名稱。使用英文逗號分隔多個名稱。",
        },
        "ko": {
            "label": "추가 모듈 (선택 사항)",
            "info": "LoRA 레이어 외에 학습 가능하게 설정할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
    },
    "rlhf_tab": {
        "en": {
            "label": "RLHF configurations",
        },
        "ru": {
            "label": "Конфигурации RLHF",
        },
        "zh": {
            "label": "RLHF 參數設定",
        },
        "ko": {
            "label": "RLHF 구성",
        },
    },
    "pref_beta": {
        "en": {
            "label": "Beta value",
            "info": "Value of the beta parameter in the loss.",
        },
        "ru": {
            "label": "Бета значение",
            "info": "Значение параметра бета в функции потерь.",
        },
        "zh": {
            "label": "Beta 參數",
            "info": "損失函數中 beta 超參數大小。",
        },
        "ko": {
            "label": "베타 값",
            "info": "손실 함수에서 베타 매개 변수의 값.",
        },
    },
    "pref_ftx": {
        "en": {
            "label": "Ftx gamma",
            "info": "The weight of SFT loss in the final loss.",
        },
        "ru": {
            "label": "Ftx гамма",
            "info": "Вес потери SFT в итоговой потере.",
        },
        "zh": {
            "label": "Ftx gamma",
            "info": "損失函數中 SFT 損失的權重大小。",
        },
        "ko": {
            "label": "Ftx 감마",
            "info": "최종 로스 함수에서 SFT 로스의 가중치.",
        },
    },
    "pref_loss": {
        "en": {
            "label": "Loss type",
            "info": "The type of the loss function.",
        },
        "ru": {
            "label": "Тип потерь",
            "info": "Тип функции потерь.",
        },
        "zh": {
            "label": "損失類型",
            "info": "損失函數的類型。",
        },
        "ko": {
            "label": "로스 유형",
            "info": "로스 함수의 유형.",
        },
    },
    "reward_model": {
        "en": {
            "label": "Reward model",
            "info": "Adapter of the reward model in PPO training.",
        },
        "ru": {
            "label": "Модель вознаграждения",
            "info": "Адаптер модели вознаграждения для обучения PPO.",
        },
        "zh": {
            "label": "獎勵模型",
            "info": "PPO 訓練中獎勵模型的adapter路徑。",
        },
        "ko": {
            "label": "리워드 모델",
            "info": "PPO 학습에서 사용할 리워드 모델의 어댑터.",
        },
    },
    "ppo_score_norm": {
        "en": {
            "label": "Score norm",
            "info": "Normalizing scores in PPO training.",
        },
        "ru": {
            "label": "Норма оценок",
            "info": "Нормализация оценок в тренировке PPO.",
        },
        "zh": {
            "label": "獎勵模型",
            "info": "PPO 訓練中歸一化獎勵分數。",
        },
        "ko": {
            "label": "스코어 정규화",
            "info": "PPO 학습에서 스코어를 정규화합니다.",
        },
    },
    "ppo_whiten_rewards": {
        "en": {
            "label": "Whiten rewards",
            "info": "Whiten the rewards in PPO training.",
        },
        "ru": {
            "label": "Белые вознаграждения",
            "info": "Осветлите вознаграждения в обучении PPO.",
        },
        "zh": {
            "label": "白化獎勵",
            "info": "PPO 訓練中將獎勵分數做白化處理。",
        },
        "ko": {
            "label": "보상 백화",
            "info": "PPO 훈련에서 보상을 백화(Whiten)합니다.",
        },
    },
    "galore_tab": {
        "en": {
            "label": "GaLore configurations",
        },
        "ru": {
            "label": "Конфигурации GaLore",
        },
        "zh": {
            "label": "GaLore 參數設定",
        },
        "ko": {
            "label": "GaLore 구성",
        },
    },
    "use_galore": {
        "en": {
            "label": "Use GaLore",
            "info": "Enable gradient low-Rank projection.",
        },
        "ru": {
            "label": "Использовать GaLore",
            "info": "Включить проекцию градиента на низкоранговое пространство.",
        },
        "zh": {
            "label": "使用 GaLore",
            "info": "使用梯度低秩投影。",
        },
        "ko": {
            "label": "GaLore 사용",
            "info": "그레디언트 로우 랭크 프로젝션을 활성화합니다.",
        },
    },
    "galore_rank": {
        "en": {
            "label": "GaLore rank",
            "info": "The rank of GaLore gradients.",
        },
        "ru": {
            "label": "Ранг GaLore",
            "info": "Ранг градиентов GaLore.",
        },
        "zh": {
            "label": "GaLore 秩",
            "info": "GaLore 梯度的秩大小。",
        },
        "ko": {
            "label": "GaLore 랭크",
            "info": "GaLore 그레디언트의 랭크.",
        },
    },
    "galore_update_interval": {
        "en": {
            "label": "Update interval",
            "info": "Number of steps to update the GaLore projection.",
        },
        "ru": {
            "label": "Интервал обновления",
            "info": "Количество шагов для обновления проекции GaLore.",
        },
        "zh": {
            "label": "更新間隔",
            "info": "相鄰兩次投影更新的步數。",
        },
        "ko": {
            "label": "업데이트 간격",
            "info": "GaLore 프로젝션을 업데이트할 간격의 스텝 수.",
        },
    },
    "galore_scale": {
        "en": {
            "label": "GaLore scale",
            "info": "GaLore scaling coefficient.",
        },
        "ru": {
            "label": "LoRA Alpha",
            "info": "Коэффициент масштабирования GaLore.",
        },
        "zh": {
            "label": "GaLore 縮放係數",
            "info": "GaLore 縮放係數大小。",
        },
        "ko": {
            "label": "GaLore 스케일",
            "info": "GaLore 스케일링 계수.",
        },
    },
    "galore_target": {
        "en": {
            "label": "GaLore modules",
            "info": "Name(s) of modules to apply GaLore. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Модули GaLore",
            "info": "Имена модулей для применения GaLore. Используйте запятые для разделения нескольких модулей.",
        },
        "zh": {
            "label": "GaLore 作用模組",
            "info": "應用 GaLore 的模組名稱。使用英文逗號分隔多個名稱。",
        },
        "ko": {
            "label": "GaLore 모듈",
            "info": "GaLore를 적용할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
    },
    "badam_tab": {
        "en": {
            "label": "BAdam configurations",
        },
        "ru": {
            "label": "Конфигурации BAdam",
        },
        "zh": {
            "label": "BAdam 參數設定",
        },
        "ko": {
            "label": "BAdam 설정",
        },
    },
    "use_badam": {
        "en": {
            "label": "Use BAdam",
            "info": "Enable the BAdam optimizer.",
        },
        "ru": {
            "label": "Использовать BAdam",
            "info": "Включите оптимизатор BAdam.",
        },
        "zh": {
            "label": "使用 BAdam",
            "info": "使用 BAdam 優化器。",
        },
        "ko": {
            "label": "BAdam 사용",
            "info": "BAdam 옵티마이저를 사용합니다.",
        },
    },
    "badam_mode": {
        "en": {
            "label": "BAdam mode",
            "info": "Whether to use layer-wise or ratio-wise BAdam optimizer.",
        },
        "ru": {
            "label": "Режим BAdam",
            "info": "Использовать ли оптимизатор BAdam с послоевой или пропорциональной настройкой.",
        },
        "zh": {
            "label": "BAdam 模式",
            "info": "使用 layer-wise 或 ratio-wise BAdam 優化器。",
        },
        "ko": {
            "label": "BAdam 모드",
            "info": "레이어-BAdam 옵티마이저인지 비율-BAdam 옵티마이저인지.",
        },
    },
    "badam_switch_mode": {
        "en": {
            "label": "Switch mode",
            "info": "The strategy of picking block to update for layer-wise BAdam.",
        },
        "ru": {
            "label": "Режим переключения",
            "info": "Стратегия выбора блока для обновления для послойного BAdam.",
        },
        "zh": {
            "label": "切換策略",
            "info": "Layer-wise BAdam 優化器的塊切換策略。",
        },
        "ko": {
            "label": "스위치 모드",
            "info": "레이어-BAdam을 위한 블록 선택 전략.",
        },
    },
    "badam_switch_interval": {
        "en": {
            "label": "Switch interval",
            "info": "Number of steps to update the block for layer-wise BAdam.",
        },
        "ru": {
            "label": "Интервал переключения",
            "info": "количество шагов для обновления блока для пошагового BAdam.",
        },
        "zh": {
            "label": "切換頻率",
            "info": "Layer-wise BAdam 優化器的塊切換頻率。",
        },
        "ko": {
            "label": "전환 간격",
            "info": "레이어-BAdam을 위한 블록 업데이트 간 스텝 수.",
        },
    },
    "badam_update_ratio": {
        "en": {
            "label": "Update ratio",
            "info": "The ratio of the update for ratio-wise BAdam.",
        },
        "ru": {
            "label": "Коэффициент обновления",
            "info": "Коэффициент обновления для BAdam с учётом соотношений.",
        },
        "zh": {
            "label": "Block 更新比例",
            "info": "Ratio-wise BAdam 優化器的更新比例。",
        },
        "ko": {
            "label": "업데이트 비율",
            "info": "비율-BAdam의 업데이트 비율.",
        },
    },
    "cmd_preview_btn": {
        "en": {
            "value": "Preview command",
        },
        "ru": {
            "value": "Просмотр команды",
        },
        "zh": {
            "value": "預覽命令",
        },
        "ko": {
            "value": "명령어 미리보기",
        },
    },
    "arg_save_btn": {
        "en": {
            "value": "Save arguments",
        },
        "ru": {
            "value": "Сохранить аргументы",
        },
        "zh": {
            "value": "保存訓練參數",
        },
        "ko": {
            "value": "Argument 저장",
        },
    },
    "arg_load_btn": {
        "en": {
            "value": "Load arguments",
        },
        "ru": {
            "value": "Загрузить аргументы",
        },
        "zh": {
            "value": "載入訓練參數",
        },
        "ko": {
            "value": "Argument 불러오기",
        },
    },
    "start_btn": {
        "en": {
            "value": "Start",
        },
        "ru": {
            "value": "Начать",
        },
        "zh": {
            "value": "開始",
        },
        "ko": {
            "value": "시작",
        },
    },
    "stop_btn": {
        "en": {
            "value": "Abort",
        },
        "ru": {
            "value": "Прервать",
        },
        "zh": {
            "value": "中斷",
        },
        "ko": {
            "value": "중단",
        },
    },
    "output_dir": {
        "en": {
            "label": "Output dir",
            "info": "Directory for saving results.",
        },
        "ru": {
            "label": "Выходной каталог",
            "info": "Каталог для сохранения результатов.",
        },
        "zh": {
            "label": "輸出目錄",
            "info": "保存結果的路徑。",
        },
        "ko": {
            "label": "출력 디렉토리",
            "info": "결과를 저장할 디렉토리.",
        },
    },
    "config_path": {
        "en": {
            "label": "Config path",
            "info": "Path to config saving arguments.",
        },
        "ru": {
            "label": "Путь к конфигурации",
            "info": "Путь для сохранения аргументов конфигурации.",
        },
        "zh": {
            "label": "配置路徑",
            "info": "保存訓練參數的設定檔路徑。",
        },
        "ko": {
            "label": "설정 경로",
            "info": "Arguments 저장 파일 경로.",
        },
    },
    "device_count": {
        "en": {
            "label": "Device count",
            "info": "Number of devices available.",
        },
        "ru": {
            "label": "Количество устройств",
            "info": "Количество доступных устройств.",
        },
        "zh": {
            "label": "設備數量",
            "info": "當前可用的運算設備數。",
        },
        "ko": {
            "label": "디바이스 수",
            "info": "사용 가능한 디바이스 수.",
        },
    },
    "ds_stage": {
        "en": {
            "label": "DeepSpeed stage",
            "info": "DeepSpeed stage for distributed training.",
        },
        "ru": {
            "label": "Этап DeepSpeed",
            "info": "Этап DeepSpeed для распределенного обучения.",
        },
        "zh": {
            "label": "DeepSpeed stage",
            "info": "多卡訓練的 DeepSpeed stage。",
        },
        "ko": {
            "label": "DeepSpeed 단계",
            "info": "분산 학습을 위한 DeepSpeed 단계.",
        },
    },
    "ds_offload": {
        "en": {
            "label": "Enable offload",
            "info": "Enable DeepSpeed offload (slow down training).",
        },
        "ru": {
            "label": "Включить выгрузку",
            "info": "включить выгрузку DeepSpeed (замедлит обучение).",
        },
        "zh": {
            "label": "使用 offload",
            "info": "使用 DeepSpeed offload（會減慢速度）。",
        },
        "ko": {
            "label": "오프로딩 활성화",
            "info": "DeepSpeed 오프로딩 활성화 (훈련 속도 느려짐).",
        },
    },
    "output_box": {
        "en": {
            "value": "Ready.",
        },
        "ru": {
            "value": "Готово.",
        },
        "zh": {
            "value": "準備就緒。",
        },
        "ko": {
            "value": "준비 완료.",
        },
    },
    "loss_viewer": {
        "en": {
            "label": "Loss",
        },
        "ru": {
            "label": "Потери",
        },
        "zh": {
            "label": "損失",
        },
        "ko": {
            "label": "손실",
        },
    },
    "predict": {
        "en": {
            "label": "Save predictions",
        },
        "ru": {
            "label": "Сохранить предсказания",
        },
        "zh": {
            "label": "保存預測結果",
        },
        "ko": {
            "label": "예측 결과 저장",
        },
    },
    "infer_backend": {
        "en": {
            "label": "Inference engine",
        },
        "ru": {
            "label": "Инференс движок",
        },
        "zh": {
            "label": "推理引擎",
        },
        "ko": {
            "label": "추론 엔진",
        },
    },
    "infer_dtype": {
        "en": {
            "label": "Inference data type",
        },
        "ru": {
            "label": "Тип данных для вывода",
        },
        "zh": {
            "label": "推理資料類型",
        },
        "ko": {
            "label": "추론 데이터 유형",
        },
    },
    "load_btn": {
        "en": {
            "value": "Load model",
        },
        "ru": {
            "value": "Загрузить модель",
        },
        "zh": {
            "value": "載入模型",
        },
        "ko": {
            "value": "모델 불러오기",
        },
    },
    "unload_btn": {
        "en": {
            "value": "Unload model",
        },
        "ru": {
            "value": "Выгрузить модель",
        },
        "zh": {
            "value": "卸載模型",
        },
        "ko": {
            "value": "모델 언로드",
        },
    },
    "info_box": {
        "en": {
            "value": "Model unloaded, please load a model first.",
        },
        "ru": {
            "value": "Модель не загружена, загрузите модель сначала.",
        },
        "zh": {
            "value": "模型未載入，請先載入模型。",
        },
        "ko": {
            "value": "모델이 언로드되었습니다. 모델을 먼저 불러오십시오.",
        },
    },
    "role": {
        "en": {
            "label": "Role",
        },
        "ru": {
            "label": "Роль",
        },
        "zh": {
            "label": "角色",
        },
        "ko": {
            "label": "역할",
        },
    },
    "system": {
        "en": {
            "placeholder": "System prompt (optional)",
        },
        "ru": {
            "placeholder": "Системный запрос (по желанию)",
        },
        "zh": {
            "placeholder": "系統提示詞（非必填）",
        },
        "ko": {
            "placeholder": "시스템 프롬프트 (선택 사항)",
        },
    },
    "tools": {
        "en": {
            "placeholder": "Tools (optional)",
        },
        "ru": {
            "placeholder": "Инструменты (по желанию)",
        },
        "zh": {
            "placeholder": "工具列表（非必填）",
        },
        "ko": {
            "placeholder": "툴 (선택 사항)",
        },
    },
    "image": {
        "en": {
            "label": "Image (optional)",
        },
        "ru": {
            "label": "Изображение (по желанию)",
        },
        "zh": {
            "label": "圖像（非必填）",
        },
        "ko": {
            "label": "이미지 (선택 사항)",
        },
    },
    "query": {
        "en": {
            "placeholder": "Input...",
        },
        "ru": {
            "placeholder": "Ввод...",
        },
        "zh": {
            "placeholder": "輸入...",
        },
        "ko": {
            "placeholder": "입력...",
        },
    },
    "submit_btn": {
        "en": {
            "value": "Submit",
        },
        "ru": {
            "value": "Отправить",
        },
        "zh": {
            "value": "提交",
        },
        "ko": {
            "value": "제출",
        },
    },
    "max_length": {
        "en": {
            "label": "Maximum length",
        },
        "ru": {
            "label": "Максимальная длина",
        },
        "zh": {
            "label": "最大長度",
        },
        "ko": {
            "label": "최대 길이",
        },
    },
    "max_new_tokens": {
        "en": {
            "label": "Maximum new tokens",
        },
        "ru": {
            "label": "Максимальное количество новых токенов",
        },
        "zh": {
            "label": "最大生成長度",
        },
        "ko": {
            "label": "응답의 최대 길이",
        },
    },
    "top_p": {
        "en": {
            "label": "Top-p",
        },
        "ru": {
            "label": "Лучшие-p",
        },
        "zh": {
            "label": "Top-p 採樣值",
        },
        "ko": {
            "label": "Top-p",
        },
    },
    "temperature": {
        "en": {
            "label": "Temperature",
        },
        "ru": {
            "label": "Температура",
        },
        "zh": {
            "label": "溫度參數",
        },
        "ko": {
            "label": "온도",
        },
    },
    "clear_btn": {
        "en": {
            "value": "Clear history",
        },
        "ru": {
            "value": "Очистить историю",
        },
        "zh": {
            "value": "清空歷史",
        },
        "ko": {
            "value": "기록 지우기",
        },
    },
    "export_size": {
        "en": {
            "label": "Max shard size (GB)",
            "info": "The maximum size for a model file.",
        },
        "ru": {
            "label": "Максимальный размер фрагмента (ГБ)",
            "info": "Максимальный размер файла модели.",
        },
        "zh": {
            "label": "最大分塊大小（GB）",
            "info": "單個模型檔的最大大小。",
        },
        "ko": {
            "label": "최대 샤드 크기 (GB)",
            "info": "모델 파일의 최대 크기.",
        },
    },
    "export_quantization_bit": {
        "en": {
            "label": "Export quantization bit.",
            "info": "Quantizing the exported model.",
        },
        "ru": {
            "label": "Экспорт бита квантования",
            "info": "Квантование экспортируемой модели.",
        },
        "zh": {
            "label": "匯出量化等級",
            "info": "量化匯出模型。",
        },
        "ko": {
            "label": "양자화 비트 내보내기",
            "info": "내보낸 모델의 양자화.",
        },
    },
    "export_quantization_dataset": {
        "en": {
            "label": "Export quantization dataset",
            "info": "The calibration dataset used for quantization.",
        },
        "ru": {
            "label": "Экспорт набора данных для квантования",
            "info": "Набор данных калибровки, используемый для квантования.",
        },
        "zh": {
            "label": "匯出量化資料集",
            "info": "量化過程中使用的校準資料集。",
        },
        "ko": {
            "label": "양자화 데이터셋 내보내기",
            "info": "양자화에 사용되는 교정 데이터셋.",
        },
    },
    "export_device": {
        "en": {
            "label": "Export device",
            "info": "Which device should be used to export model.",
        },
        "ru": {
            "label": "Экспорт устройство",
            "info": "Какое устройство следует использовать для экспорта модели.",
        },
        "zh": {
            "label": "匯出裝置",
            "info": "匯出模型使用的裝置類型。",
        },
        "ko": {
            "label": "내보낼 장치",
            "info": "모델을 내보내는 데 사용할 장치.",
        },
    },
    "export_legacy_format": {
        "en": {
            "label": "Export legacy format",
            "info": "Do not use safetensors to save the model.",
        },
        "ru": {
            "label": "Экспорт в устаревший формат",
            "info": "Не использовать safetensors для сохранения модели.",
        },
        "zh": {
            "label": "匯出舊格式",
            "info": "不使用 safetensors 格式保存模型。",
        },
        "ko": {
            "label": "레거시 형식 내보내기",
            "info": "모델을 저장하는 데 safetensors를 사용하지 않습니다.",
        },
    },
    "export_dir": {
        "en": {
            "label": "Export dir",
            "info": "Directory to save exported model.",
        },
        "ru": {
            "label": "Каталог экспорта",
            "info": "Каталог для сохранения экспортированной модели.",
        },
        "zh": {
            "label": "匯出目錄",
            "info": "保存匯出模型的資料夾路徑。",
        },
        "ko": {
            "label": "내보내기 디렉토리",
            "info": "내보낸 모델을 저장할 디렉토리.",
        },
    },
    "export_hub_model_id": {
        "en": {
            "label": "HF Hub ID (optional)",
            "info": "Repo ID for uploading model to Hugging Face hub.",
        },
        "ru": {
            "label": "HF Hub ID (опционально)",
            "info": "Идентификатор репозитория для загрузки модели на Hugging Face hub.",
        },
        "zh": {
            "label": "HF Hub ID（非必填）",
            "info": "用於將模型上傳至 Hugging Face Hub 的倉庫 ID。",
        },
        "ko": {
            "label": "HF 허브 ID (선택 사항)",
            "info": "모델을 Hugging Face 허브에 업로드하기 위한 레포 ID.",
        },
    },
    "export_btn": {
        "en": {
            "value": "Export",
        },
        "ru": {
            "value": "Экспорт",
        },
        "zh": {
            "value": "開始匯出",
        },
        "ko": {
            "value": "내보내기",
        },
    },
}


ALERTS = {
    "err_conflict": {
        "en": "A process is in running, please abort it first.",
        "ru": "Процесс уже запущен, пожалуйста, сначала прервите его.",
        "zh": "任務已存在，請先中斷訓練。",
        "ko": "프로세스가 실행 중입니다. 먼저 중단하십시오.",
    },
    "err_exists": {
        "en": "You have loaded a model, please unload it first.",
        "ru": "Вы загрузили модель, сначала разгрузите ее.",
        "zh": "模型已存在，請先卸載模型。",
        "ko": "모델이 로드되었습니다. 먼저 언로드하십시오.",
    },
    "err_no_model": {
        "en": "Please select a model.",
        "ru": "Пожалуйста, выберите модель.",
        "zh": "請選擇模型。",
        "ko": "모델을 선택하십시오.",
    },
    "err_no_path": {
        "en": "Model not found.",
        "ru": "Модель не найдена.",
        "zh": "模型未找到。",
        "ko": "모델을 찾을 수 없습니다.",
    },
    "err_no_dataset": {
        "en": "Please choose a dataset.",
        "ru": "Пожалуйста, выберите набор данных.",
        "zh": "請選擇資料集。",
        "ko": "데이터 세트를 선택하십시오.",
    },
    "err_no_adapter": {
        "en": "Please select an adapter.",
        "ru": "Пожалуйста, выберите адаптер.",
        "zh": "請選擇 adapter。",
        "ko": "어댑터를 선택하십시오.",
    },
    "err_no_output_dir": {
        "en": "Please provide output dir.",
        "ru": "Пожалуйста, укажите выходную директорию.",
        "zh": "請填寫輸出目錄。",
        "ko": "출력 디렉토리를 제공하십시오.",
    },
    "err_no_reward_model": {
        "en": "Please select a reward model.",
        "ru": "Пожалуйста, выберите модель вознаграждения.",
        "zh": "請選擇獎勵模型。",
        "ko": "리워드 모델을 선택하십시오.",
    },
    "err_no_export_dir": {
        "en": "Please provide export dir.",
        "ru": "Пожалуйста, укажите каталог для экспорта.",
        "zh": "請填寫匯出目錄。",
        "ko": "Export 디렉토리를 제공하십시오.",
    },
    "err_gptq_lora": {
        "en": "Please merge adapters before quantizing the model.",
        "ru": "Пожалуйста, объедините адаптеры перед квантованием модели.",
        "zh": "量化模型前請先合併 adapter。",
        "ko": "모델을 양자화하기 전에 어댑터를 병합하십시오.",
    },
    "err_failed": {
        "en": "Failed.",
        "ru": "Ошибка.",
        "zh": "訓練出錯。",
        "ko": "실패했습니다.",
    },
    "err_demo": {
        "en": "Training is unavailable in demo mode, duplicate the space to a private one first.",
        "ru": "Обучение недоступно в демонстрационном режиме, сначала скопируйте пространство в частное.",
        "zh": "展示模式不支援訓練，請先複製到其他空間。",
        "ko": "데모 모드에서는 훈련을 사용할 수 없습니다. 먼저 프라이빗 레포지토리로 작업 공간을 복제하십시오.",
    },
    "err_tool_name": {
        "en": "Tool name not found.",
        "ru": "Имя инструмента не найдено.",
        "zh": "未找到工具名稱。",
        "ko": "툴 이름을 찾을 수 없습니다.",
    },
    "err_json_schema": {
        "en": "Invalid JSON schema.",
        "ru": "Неверная схема JSON.",
        "zh": "Json 格式錯誤。",
        "ko": "잘못된 JSON 스키마입니다.",
    },
    "err_config_not_found": {
        "en": "Config file is not found.",
        "ru": "Файл конфигурации не найден.",
        "zh": "未找到設定檔。",
        "ko": "Config 파일을 찾을 수 없습니다.",
    },
    "warn_no_cuda": {
        "en": "CUDA environment was not detected.",
        "ru": "Среда CUDA не обнаружена.",
        "zh": "未檢測到 CUDA 環境。",
        "ko": "CUDA 환경이 감지되지 않았습니다.",
    },
    "warn_output_dir_exists": {
        "en": "Output dir already exists, will resume training from here.",
        "ru": "Выходной каталог уже существует, обучение будет продолжено отсюда.",
        "zh": "輸出目錄已存在，將從該中斷點恢復訓練。",
        "ko": "출력 디렉토리가 이미 존재합니다. 위 출력 디렉토리에 저장된 학습을 재개합니다.",
    },
    "info_aborting": {
        "en": "Aborted, wait for terminating...",
        "ru": "Прервано, ожидание завершения...",
        "zh": "訓練中斷，正在等待進程結束……",
        "ko": "중단되었습니다. 종료를 기다리십시오...",
    },
    "info_aborted": {
        "en": "Ready.",
        "ru": "Готово.",
        "zh": "準備就緒。",
        "ko": "준비되었습니다.",
    },
    "info_finished": {
        "en": "Finished.",
        "ru": "Завершено.",
        "zh": "訓練完畢。",
        "ko": "완료되었습니다.",
    },
    "info_config_saved": {
        "en": "Arguments have been saved at: ",
        "ru": "Аргументы были сохранены по адресу: ",
        "zh": "訓練參數已保存至：",
        "ko": "매개변수가 저장되었습니다: ",
    },
    "info_config_loaded": {
        "en": "Arguments have been restored.",
        "ru": "Аргументы были восстановлены.",
        "zh": "訓練參數已載入。",
        "ko": "매개변수가 복원되었습니다.",
    },
    "info_loading": {
        "en": "Loading model...",
        "ru": "Загрузка модели...",
        "zh": "載入中……",
        "ko": "모델 로딩 중...",
    },
    "info_unloading": {
        "en": "Unloading model...",
        "ru": "Выгрузка модели...",
        "zh": "卸載中……",
        "ko": "모델 언로딩 중...",
    },
    "info_loaded": {
        "en": "Model loaded, now you can chat with your model!",
        "ru": "Модель загружена, теперь вы можете общаться с вашей моделью!",
        "zh": "模型已載入，可以開始聊天了！",
        "ko": "모델이 로드되었습니다. 이제 모델과 채팅할 수 있습니다!",
    },
    "info_unloaded": {
        "en": "Model unloaded.",
        "ru": "Модель выгружена.",
        "zh": "模型已卸載。",
        "ko": "모델이 언로드되었습니다.",
    },
    "info_exporting": {
        "en": "Exporting model...",
        "ru": "Экспорт модели...",
        "zh": "正在匯出模型……",
        "ko": "모델 내보내기 중...",
    },
    "info_exported": {
        "en": "Model exported.",
        "ru": "Модель экспортирована.",
        "zh": "模型匯出完成。",
        "ko": "모델이 내보내졌습니다.",
    },
}
