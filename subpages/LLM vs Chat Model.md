# LLM vs. Chat Model

![image.png](../assets/LLM vs Chat Model/image.png)

這張圖描述 LangChain 中 **LLM** 和 **Chat Model** 的互動和輸入/輸出

1. **輸入格式**：
    - **LLM 和 Chat Model 都可以接受以下三種類型的輸入**：
        - **text**：直接傳遞簡單的字符串輸入，例如 `"I need help."`。
        - **Messages**：包括類似 `HumanMessage`, `SystemMessage`, 和 `AIMessage` 等結構化消息類型，用於更細緻的對話上下文建模。
        - **Prompt**：可以是 `str` 或 LangChain 的 `PromptValue` 格式，例如結構化的 Prompt 用於生成更具上下文的輸出。
2. **模型選擇**：
    - **LLM** 是一個基礎語言模型，適合處理簡單的輸入，例如字符串或單一的 Prompt。
    - **Chat Model** 是針對多輪對話進行優化的模型，能處理更複雜的結構化輸入（如一組消息）。
3. **輸出格式**：
    - **LLM**：
        - 輸出默認為字符串（`str`），但可以通過特定的設置或包裝轉換為 `AIMessage`。
        - **正確結論**：LLM 的輸出主要是字符串，但可以被進一步封裝成其他格式。
    - **Chat Model**：
        - 輸出默認為 `AIMessage`（結構化的消息類型）。
        - 可以通過調用 `.text` 或其他方法轉換為純字符串。
4. **方法**：
    - **invoke()**：用於生成模型輸出（推薦使用）。無論是 LLM 還是 Chat Model，都可以調用 `.invoke()` 方法來產生結果。
    - **generate()**：也可以用於生成輸出，但在某些情況下不如 `.invoke()` 高效，因為 `.invoke()` 更適合 LangChain 的框架設計。
5. **關鍵點補充**：
    - 圖片中提到的 **BaseMessages** 是 LangChain 定義的基礎消息類型，它們被用於定義對話的上下文。
    - **ChatPromptValue** 和 **StrPromptValue** 是 Prompt 的進一步封裝，用於支持不同格式的輸入處理。