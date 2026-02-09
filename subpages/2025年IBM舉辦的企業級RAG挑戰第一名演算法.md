# 2025年IBM舉辦的企業級RAG挑戰第一名演算法

2025年IBM舉辦的企業級RAG挑戰賽中，Ilya Rice設計的系統橫掃雙料冠軍，該系統能精準回答問題並提供可靠來源頁碼，有效避免AI幻覺問題。🌟

系統特色：

🏗️ 高效PDF處理：採用客製化Docling處理PDF文件，保留表格結構與格式。透過GPU加速，系統在2.5小時內完成100份千頁年報的解析。

💾 獨立向量資料庫：為每家公司建立獨立資料庫，避免混雜資訊並縮減搜尋範圍。系統將文字分成300個Tokens的小區塊，保留50個Tokens的重疊區域，並使用text-embedding-3-large模型向量化。

🔍 雙重路由與重排序：系統識別問題中的公司名稱，只在該公司資料庫搜尋，縮小搜尋空間100倍，並透過GPT-4o-mini進行LLM重排序。

📄 父頁面檢索：系統不直接使用找到的小區塊，而是將它們作為指標獲取完整頁面，確保關鍵資訊完整獲取。

💡 智慧答案生成：根據問題類型使用不同提示範本，採用結構化輸出與思考鏈，讓模型逐步分析問題。

系統不僅與OpenAI模型相容，使用Llama 3.3 70b也能達到相近效果。甚至8b模型也超越80%參賽者系統表現。🚀

作者分享：
[https://abdullin.com/ilya/how-to-build-best-rag/](https://abdullin.com/ilya/how-to-build-best-rag/)

開源程式碼：
[https://github.com/IlyaRice/RAG-Challenge-2](https://github.com/IlyaRice/RAG-Challenge-2)

DeepWiki：
[https://deepwiki.com/IlyaRice/RAG-Challenge-2](https://deepwiki.com/IlyaRice/RAG-Challenge-2)