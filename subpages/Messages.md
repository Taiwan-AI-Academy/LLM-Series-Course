# Messages

![image.png](Messages/image.png)

## **1. Messages 的核心概念**

- **Messages 是 Chat Model 中的基本溝通單元**，由三個核心組成部分：
    - **Role (角色)**：定義消息的來源或功能，例如 `user`、`assistant`。
    - **Content (內容)**：消息的實際內容（文字或數據）。
    - **Metadata (元數據)**：可選，提供額外的上下文信息（不一定需要，但可用於進階功能）。

---

## **2. Messages 的主要類型**

LangChain 使用基於 `BaseMessage` 的不同類型來組織消息，每種類型的用途如下：

### **2.1 HumanMessage**

- **定義**：由用戶發送的消息。
- **用途**：表示用戶的輸入，例如問題、指令或請求。
- **格式**：
    - 使用 `kwargs` 或純字符串 (`str`)。
    - **範例**：
        
        ```python
        from langchain.schema import HumanMessage
        
        user_message = HumanMessage(content="What is the weather today?")
        ```
        

### **2.2 SystemMessage**

- **定義**：由系統提供的上下文消息。
- **用途**：指導模型的行為，例如告訴模型應如何回應或提供額外的背景。
- **特點**：並非所有 Chat Model 提供者都支持此類型。
- **範例**：
    
    ```python
    from langchain.schema import SystemMessage
    
    system_message = SystemMessage(content="You are a helpful assistant.")
    ```
    

### **2.3 AIMessage**

- **定義**：由 AI 模型生成的回應消息。
- **用途**：代表模型對用戶輸入的回應。
- **格式**：
    - 使用 `kwargs` 或純字符串 (`str`)。
    - **範例**：
        
        ```python
        from langchain.schema import AIMessage
        
        ai_message = AIMessage(content="The weather today is sunny.")
        ```
        

### **2.4 Tool Message (工具消息)**

- **定義**：將外部工具（例如 API）調用結果返回給模型的消息。
- **用途**：
    - 用於支持工具調用的 Chat Model。
    - 將外部數據（如檢索結果）傳遞回模型。
- **特點**：
    - 僅在支持 **Tool Calling** 功能的模型中使用。

---

## **3. Role 與其描述**

圖中的表格列出了消息類型的 **Role** 和功能描述：

| **Role** | **Description** |
| --- | --- |
| **system** | 提供上下文，指導模型的行為，例如設置模型的角色或提供額外資訊。 |
| **user** | 用戶的輸入，與模型的主要交互方式。 |
| **assistant** | 模型生成的回應，通常是對用戶輸入的答案或反應。 |
| **tool** | 外部工具返回的數據，例如檢索結果或計算結果，用於進一步處理。 |

---

## **4. BaseMessage 的特性與最佳實踐**

### **4.1 特性**

- **BaseMessage** 是所有消息類型的基礎類別。
- **限制**：不像 `PromptTemplate` 那樣支持動態變數插值。
    - **提示**：需要動態內容時，請考慮使用 `PromptTemplate`。

### **4.2 最佳實踐**

- **將單條消息作為列表使用**：
    - 即使只需要傳遞一條消息，也應將其封裝為 `list[BaseMessage]`。
    - **原因**：許多接口要求消息的輸入格式為消息列表。
    - **範例**：
        
        ```python
        from langchain.schema import HumanMessage
        
        messages = [HumanMessage(content="What is the weather today?")]
        ```
        

---

## **5. 提示與補充**

1. **BaseMessage 限制**：
    - 無法像 `PromptTemplate` 一樣接受輸入變數。
    - 適合靜態消息內容，而非需要插值的動態場景。
2. **建議封裝為列表**：
    - 即使只有單一消息，也應該以 `list` 的形式提供，方便與 LangChain 的其他功能（如對話上下文）無縫結合。

---

## **6. 使用場景與應用**

### **6.1 多輪對話**

- 將多條消息（如 SystemMessage、HumanMessage 和 AIMessage）組成列表，作為 Chat Model 的上下文。
    
    ```python
    from langchain.schema import HumanMessage, SystemMessage, AIMessage
    
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Tell me a joke."),
        AIMessage(content="Sure, here's a joke: Why did the chicken cross the road?")
    ]
    ```
    

### **6.2 Tool Integration**

- 結合 Tool Message，將外部數據作為模型輸入的一部分。
    
    ```python
    tool_message = ToolMessage(content="API result: 25°C")
    ```
    

---

## **總結**

1. **Messages 是 LangChain 與 Chat Model 交互的核心結構**，支持靈活的多角色設置。
2. **BaseMessage 的子類**（如 HumanMessage、SystemMessage）提供了清晰的消息類型分類。
3. **最佳實踐**：即使是單一消息，也應該以 `list[BaseMessage]` 的格式封裝，以保證與接口的兼容性。
4. **限制與擴展**：BaseMessage 適合靜態消息，但動態內容應使用 PromptTemplate。