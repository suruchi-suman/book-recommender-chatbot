# 🕮 Book Recommender Chatbot using IBM Watson Assistant

An AI-powered virtual assistant designed to help readers discover books based on their preferences using **IBM Watson Assistant**. This chatbot recommends books based on genres, moods, authors, budget, and more. It also includes fun features like book trivia, witty puns, and even a virtual bookstore tour!

---

## 🕮 Features

- Personalized book recommendations (by genre, author, mood, budget, etc.)
- Smart dialog flow using Watson Assistant
- Fun interactions (book puns, facts, fortunes)
- Virtual bookstore tour (via iframe)
- Seamless web chat integration

---

## 🕮 Built With

- IBM Watson Assistant
- HTML/CSS (for web embedding)
- Watson Assistant Web Chat

---

## 🕮 How to Reproduce This Project

### Step 1: Set Up Watson Assistant

1. Log in to [IBM Cloud](https://cloud.ibm.com)
2. Search for **Watson Assistant** and create a new instance
3. Launch Watson Assistant from your dashboard
4. Activate dialog under **Settings > Dialog**

### Step 2: Create Your Dialog Flow

- Create **Intents** like `#recommend_book`, `#book_fun_fact`, `#book_fortune`, etc.
- Create **Entities** like `@genre`, `@mood`, `@budget`
- Design **Dialog Nodes** for:
  - Book recommendations
  - Fun facts
  - Subgenre selections
  - Virtual tour
- Use **child nodes** to manage sub-flows (e.g., Fiction → Fantasy)

### Step 3: Customize and Publish

- Go to `Customize Web Chat` and design your bot’s appearance
- Click on **Publish**
- Choose the **Live** environment
- Copy the embed HTML code

### Step 4: Embed in Website

Paste the Watson Assistant embed code **before `</body>`** tag in your HTML file.

```html
<!-- IBM Watson Assistant Embed Code -->
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "your-integration-id", // Replace with your ID
    region: "your-region", // e.g., "us-south"
    serviceInstanceID: "your-service-id",
    onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function() {
    const t = document.createElement('script');
    t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/loadWatsonAssistantChat.js";
    document.head.appendChild(t);
  });
</script>
```

### Step 5: Deployment with GitHub Pages

Follow these steps to deploy your chatbot website using **GitHub Pages**:

1. **Create a GitHub Repository**
   - Go to [GitHub](https://github.com) and create a new repository.
   - Name it anything you like (e.g., `book-recommender-chatbot`).
   - Make sure to initialize it with a `README.md`.

2. **Upload Your Project Files**
   - Add your HTML, CSS, JavaScript, and any other required files to the repository.
   - Make sure your main HTML file is named `index.html`.

3. **Commit and Push Changes**

4. **Enable GitHub Pages**
   - Go to **Settings** in your repository.
   - Scroll down to the **Pages** section.
   - Under **Source**, select `main` branch and `/ (root)` folder.
   - Click **Save**.

5. **Access Your Live Website**
   - GitHub will provide a deployment URL in the Pages section.
   - Example: `https://your-username.github.io/book-recommender-chatbot`

   **Tip:** If your site isn’t showing updated changes, clear your browser cache or do a hard refresh (`Ctrl + Shift + R`).


