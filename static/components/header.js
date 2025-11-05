// header.js
class MedHeader extends HTMLElement {
  constructor() {
    super();

    // Shadow DOM oluşturuyoruz (izole stil ve içerik)
    const shadow = this.attachShadow({ mode: "open" });

    // Template
    const wrapper = document.createElement("header");
    wrapper.innerHTML = `
      <style>
        header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 20px 80px;
          background-color: rgba(0, 0, 0, 0.8);
          border-bottom: 0.5px solid #8660ba;
          font-family: 'Inter', sans-serif;
        }

        .logo {
          font-weight: 700;
          font-size: 1.3rem;
          background: linear-gradient(90deg, #00aaff, #8660ba);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }

        nav ul {
          list-style: none;
          display: flex;
          gap: 30px;
          margin: 0;
          padding: 0;
        }

        nav a {
          text-decoration: none;
          color: #cfd8e3;
          font-weight: 500;
        }

        nav a:hover {
          color: #8660ba;
        }

        .btn-outline {
          background-color: transparent;
          color: #00aaff;
          border: 2px solid transparent;
          border-radius: 6px;
          padding: 8px 20px;
          cursor: pointer;
          transition: all 0.3s ease;
          background-image: linear-gradient(#0a0f1f, #0a0f1f),
              linear-gradient(90deg, #00aaff, #8660ba);
          background-origin: border-box;
          background-clip: padding-box, border-box;
        }

        .btn-outline:hover {
          color: #fff;
          background-image: linear-gradient(90deg, #00aaff, #8660ba);
          box-shadow: 0 0 15px rgba(134, 96, 186, 0.5);
          transform: translateY(-2px);
        }
      </style>

      <div class="logo"><a href="index.html">⚕️ MedNexus</a></div>
      <nav>
        <ul>
          <li><a href="about.html">About Team</a></li>
          <li><a href="login.html" class="btn-outline">Login</a></li>
        </ul>
      </nav>
    `;

    shadow.appendChild(wrapper);
  }

  // Eğer dinamik attribute ile link eklemek istersen (örn. data-links)
  static get observedAttributes() {
    return ["data-links"];
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (name === "data-links" && newValue) {
      const links = JSON.parse(newValue);
      const nav = this.shadowRoot.querySelector("nav ul");
      nav.innerHTML = ""; // mevcut linkleri temizle
      links.forEach(link => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${link.href}">${link.label}</a>`;
        nav.appendChild(li);
      });
    }
  }
}

customElements.define("med-header", MedHeader);
