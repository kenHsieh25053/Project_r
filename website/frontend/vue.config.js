module.exports = {
    baseUrl: '/', // 部署應用時的根路徑(默認'/'),也可用相對路徑(存在使用限制)
    // outputDir: 'dist', // 運行時生成的生產環境構建文件的目錄(默認''dist''，構建之前會被清除)
    assetsDir: 'static', //放置生成的靜態資源(s、css、img、fonts)的(相對於 outputDir 的)目錄(默認'')
    indexPath: 'index.html', //指定生成的 index.html 的輸出路徑(相對於 outputDir)也可以是一個絕對路徑。
    pages: { //pages 裡配置的路徑和文件名在你的文檔目錄必須存在 否則啟動服務會報錯
        index: { //除了 entry 之外都是可選的
            entry: 'src/main.js', // page 的入口,每個“page”應該有一個對應的 JavaScript 入口文件
            template: 'public/index.html', // 模板來源
            filename: 'index.html', // 在 dist/index.html 的輸出
            title: 'Index Page', // 當使用 title 選項時,在 template 中使用：<title><%= htmlWebpackPlugin.options.title %></title>
            chunks: ['chunk-vendors', 'chunk-common', 'index'] // 在這個頁面中包含的塊，默認情況下會包含,提取出來的通用 chunk 和 vendor chunk
        },
        // subpage: 'src/subpage/main.js' //官方解釋：當使用只有入口的字符串格式時,模板會被推導為'public/subpage.html',若找不到就回退到'public/index.html',輸出文件名會被推導為'subpage.html'
    },
    lintOnSave: true, // 是否在保存的時候檢查
    productionSourceMap: true, // 生產環境是否生成 sourceMap 文件
    css: {
        extract: true, // 是否使用css分離插件 ExtractTextPlugin
        sourceMap: false, // 開啟 CSS source maps
        loaderOptions: {}, // css預設器配置項
        modules: false // 啟用 CSS modules for all css / pre-processor files.
    },
    devServer: { // 環境配置
        host: 'localhost',
        port: 8080,
        https: false,
        hotOnly: false,
        open: true, //配置自動啟動瀏覽器
        proxy: { // 配置多個代理(配置一個 proxy: 'http://localhost:4000' )
            '/api': {
                target: '<url>',
                ws: true,
                changeOrigin: true
            },
            '/foo': {
                target: '<other_url>'
            }
        },
    },
    pluginOptions: { // 第三方插件配置
        // ...
    },
};