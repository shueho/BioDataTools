// 新标签页打开工具链接
function openPage(url) {
    window.open(url, '_blank');
}

// 平滑滚动到对应分类区块
function scrollToCate(id) {
    const target = document.getElementById(id);
    if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
    }
}

// 渲染页面所有内容 + 左侧折叠菜单
function renderAll() {
    const toolWrapper = document.getElementById('toolList');
    const navWrapper = document.getElementById('navList');
    let toolHtml = '';
    let navHtml = '';

    toolConfig.forEach((cate, idx) => {
        const cateId = `cate_${idx}`;
        const subMenuId = `sub_menu_${idx}`;

        // 渲染右侧工具卡片
        toolHtml += `<div class="tool-category" id="${cateId}">
            <h3 class="category-title">
                <span class="category-icon">${cate.categoryIcon}</span>
                ${cate.categoryName}
            </h3>
            <div class="sub-tool-grid">`;

        cate.tools.forEach(tool => {
            toolHtml += `<div class="sub-tool-card" onclick="openPage('${tool.link}')">
                <div class="icon">${tool.toolIcon}</div>
                <h4>${tool.toolName}</h4>
                <p>${tool.toolDesc}</p>
            </div>`;
        });

        toolHtml += `</div></div>`;

        // 渲染左侧折叠导航
        navHtml += `
        <li>
            <a class="parent-item">${cate.categoryName}</a>
            <ul class="sub-menu" id="${subMenuId}">
        `;
        cate.tools.forEach(tool => {
            navHtml += `<li><a onclick="scrollToCate('${cateId}')">${tool.toolName}</a></li>`;
        });
        navHtml += `</ul></li>`;
    });

    toolWrapper.innerHTML = toolHtml;
    navWrapper.innerHTML = navHtml;
}

// DOM加载完成执行渲染
document.addEventListener('DOMContentLoaded', renderAll);

// 菜单展开/折叠交互（事件委托，兼容动态DOM）
const navList = document.getElementById('navList');
navList.addEventListener('click', function (e) {
    if (e.target.classList.contains('parent-item')) {
        const subMenu = e.target.nextElementSibling;
        subMenu.classList.toggle('open');
        e.stopPropagation();
    }
});