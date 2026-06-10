// 渲染左侧导航栏
function renderSideNav() {
    const navList = document.getElementById('navList');
    navList.innerHTML = '';

    // 博客首页
    const blogItem = document.createElement('li');
    blogItem.innerHTML = `
        <a href="blog/home.html" class="parent-item blog-home-item">
            📝 博客首页
        </a>
    `;
    navList.appendChild(blogItem);

    // 在线科研绘图 ==========
    const plotItem = document.createElement('li');
    plotItem.innerHTML = `
        <a href="plot/home.html" target="_blank" class="parent-item blog-home-item">
            🎨 在线科研绘图
        </a>
    `;
    navList.appendChild(plotItem);

    // 渲染分类导航
    toolConfig.forEach((category, catIndex) => {
        const categoryItem = document.createElement('li');
        const subMenuId = `submenu-${catIndex}`;
        categoryItem.innerHTML = `
            <a class="parent-item" onclick="toggleSubMenu(${catIndex})">
                ${category.categoryIcon} ${category.categoryName}
            </a>
            <ul class="sub-menu" id="${subMenuId}"></ul>
        `;
        navList.appendChild(categoryItem);

        const subMenu = document.getElementById(subMenuId);
       
        category.tools.forEach((tool, toolIndex) => {
            const toolId = `tool-${catIndex}-${toolIndex}`;
            const toolItem = document.createElement('li');
            let iconText = tool.toolIcon.includes('images/') ? '' : tool.toolIcon;
            toolItem.innerHTML = `
                <a onclick="scrollToTool('${toolId}')">
                    ${iconText} ${tool.toolName}
                </a>
            `;
            subMenu.appendChild(toolItem);
        });
    });
}

// 展开/收起子菜单
function toggleSubMenu(catIndex) {
    const subMenu = document.getElementById(`submenu-${catIndex}`);
    subMenu.classList.toggle('open');
}

// 平滑滚动定位
function scrollToTool(toolId) {
    const targetEl = document.getElementById(toolId);
    if (targetEl) {
        // 计算偏移量：header高度(约100px) + 额外留白(20px)
        const headerHeight = document.querySelector('header').offsetHeight || 100;
        const offsetTop = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
        window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
        });
    }
}

// 渲染主内容工具卡片
function renderToolList() {
    const toolList = document.getElementById('toolList');
    toolList.innerHTML = '';

    toolConfig.forEach((category, catIndex) => {
        const catWrap = document.createElement('div');
        catWrap.className = 'tool-category';
        catWrap.innerHTML = `
            <div class="category-title">
                <span class="category-icon">${category.categoryIcon}</span>
                <h3>${category.categoryName}</h3>
            </div>
            <div class="sub-tool-grid" id="grid-${catIndex}"></div>
        `;
        toolList.appendChild(catWrap);

        const grid = document.getElementById(`grid-${catIndex}`);
        category.tools.forEach((tool, toolIndex) => {
            const toolId = `tool-${catIndex}-${toolIndex}`;
            const card = document.createElement('div');
            card.className = 'sub-tool-card';
            card.id = toolId;

            
            let iconHtml = '';
            if (tool.toolIcon.startsWith('images/')) {
                iconHtml = `<img src="${tool.toolIcon}" alt="${tool.toolName}">`;
            } else {
                iconHtml = tool.toolIcon;
            }

            card.innerHTML = `
                <div class="icon">${iconHtml}</div>
                <h4>${tool.toolName}</h4>
                <p>${tool.toolDesc}</p>
            `;
            //不新开card.onclick = () => window.location.href = tool.link;
            card.onclick = () => window.open(tool.link, '_blank');
            grid.appendChild(card);
        });
    });
}

// 页面加载执行
window.addEventListener('DOMContentLoaded', function () {
    renderSideNav();
    renderToolList();
});