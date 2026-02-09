# String Output Parser

![image.png](String%20Output%20Parser/image.png)

這張圖展示了 **`StrOutputParser`** 的概念與應用場景，主要用於將模型的輸出（例如 `AIMessage` 或文字）直接轉換為字符串，並保證輸出內容不經過任何改變。以下是對該圖的詳細解釋：

---

## **1. `StrOutputParser` 的作用**

- **目的**：將來自模型（LLM 或 Chat Model）的輸出，無論是 `AIMessage` 還是純文字，轉換成字符串。
- **關鍵點**：不對輸入進行任何變更，直接返回原始輸入作為輸出。

---

## **2. 方法解析**

### **2.1 `parse()` 方法**

- **作用**：接受純字符串作為輸入，直接返回相同的字符串。
- **輸入輸出格式**：
    
    ```
    str_parser.parse(input: str) → str
    ```
    
- **範例**：
    
    ```python
    from langchain.output_parsers import StrOutputParser
    
    str_parser = StrOutputParser()
    result = str_parser.parse("Sure, how can I help you?")
    print(result)  # 輸出: "Sure, how can I help you?"
    ```
    

### **2.2 `invoke()` 方法**

- **作用**：接受字符串或 `BaseMessage`（如 `AIMessage`）作為輸入，將其轉換為字符串並返回。
- **輸入輸出格式**：
    
    ```
    str_parser.invoke(input: str | BaseMessage) → str
    ```
    
- **範例**：
    
    ```python
    from langchain.schema import AIMessage
    
    str_parser = StrOutputParser()
    result = str_parser.invoke(AIMessage(content="Sure, how can I help you?"))
    print(result)  # 輸出: "Sure, how can I help you?"
    ```
    

---

## **3. 圖中的流程解釋**

### **3.1 輸入 (Input)**

- 可以是：
    - **Prompt**（用戶輸入的問題或請求）：例如 `"I need help."`

### **3.2 模型處理 (Model)**

- 可以是：
    - **LLM（基礎語言模型）**
    - **Chat Model（針對對話優化的語言模型）**
- 通過 `.invoke()` 方法，模型將輸入的 Prompt 處理並生成輸出。

### **3.3 輸出 (Output)**

- 模型的輸出可能是：
    1. **純文本**（`text`）：例如 `"\n\nSure, how can I help you?"`
    2. **結構化消息**（`AIMessage`）：例如：
        
        ```python
        AIMessage(content="Sure, how can I help you?")
        ```
        

### **3.4 使用 `StrOutputParser` 處理輸出**

- 通過 **`str_parser.parse()` 或 `str_parser.invoke()`**，將輸出轉換為純字符串。
- 最終結果不變，例如：
    
    ```
    "Sure, how can I help you?"
    ```
    

---

## **4. 應用場景**

`StrOutputParser` 適用於以下場景：

1. **簡單的文本處理**：
    - 如果模型輸出的內容不需要進一步結構化處理，只需要純文本輸出。
    - 範例：直接返回模型生成的回應作為用戶界面的輸出。
2. **多模型輸出處理一致性**：
    - 在處理多種模型（LLM 或 Chat Model）時，將不同輸出統一為字符串格式，方便後續處理。
3. **消息提取**：
    - 如果模型返回的是 `AIMessage`，需要提取其中的 `content` 作為字符串。

---

## **5. 特點**

- **簡單直接**：`StrOutputParser` 不對輸出進行任何改變，僅提取或轉換為字符串。
- **靈活兼容**：既支持純文本，又支持結構化消息（如 `AIMessage`）。

---

## **6. 總結**

- **`StrOutputParser` 是最基本的解析器**，適用於簡單場景，不對輸出進行任何變更。
- 提供 `.parse()` 和 `.invoke()` 兩種方法，適應不同的輸入類型。
- 適合用於純文本返回需求的應用，如用戶界面展示或基礎的結果處理。