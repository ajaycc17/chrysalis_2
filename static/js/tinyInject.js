var script = document.createElement('script');
script.type = 'text/javascript';
script.referrerPolicy= "origin";
script.src= "https://cdn.tiny.cloud/1/w0dnoedqus44dang0u1zlt62jdrg5u0ezxrm9ala73p83qjv/tinymce/5/tinymce.min.js";

document.head.appendChild(script);

script.onload = function () {
    tinymce.init({
        selector: '#id_content',
        height: 550,
        plugins: [
            'responsiveImage', 'toc', 'quickbars',
            'advlist autolink link image lists charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'table emoticons template paste help', 'codesample'
        ],
        codesample_languages: [
            { text: 'HTML/XML', value: 'markup' },
            { text: 'JavaScript', value: 'javascript' },
            { text: 'CSS', value: 'css' },
            { text: 'PHP', value: 'php' },
            { text: 'Ruby', value: 'ruby' },
            { text: 'Python', value: 'python' },
            { text: 'Java', value: 'java' },
            { text: 'C', value: 'c' },
            { text: 'C#', value: 'csharp' },
            { text: 'C++', value: 'cpp' },
            { text: 'Shell', value: 'shell' },
            { text: 'Arduino', value: 'arduino' },
            { text: 'ASP.NET', value: 'aspnet' },
            { text: 'Djano/Jinja2', value: 'django' },
            { text: 'Docker', value: 'docker' },
            { text: 'Git', value: 'git' },
            { text: 'Go', value: 'go' },
            { text: 'MongoDB', value: 'mongodb' },
            { text: 'MATLAB', value: 'matlab' },
            { text: 'Kotlin', value: 'kotlin' },
            { text: 'JSON', value: 'json' },
            { text: 'GitIgnore', value: 'ignore' },
            { text: 'GraphQL', value: 'graphql' },
            { text: 'React JSX', value: 'jsx' },
            { text: 'SCSS', value: 'scss' },
            { text: 'SQL', value: 'sql' },
            { text: 'TypeScript', value: 'typescript' },
            { text: 'Vim', value: 'vim' },
            { text: 'VHDL', value: 'vhdl' },
          ],
        toolbar: 'undo redo | toc | styleselect | codesample | bold italic | alignleft aligncenter alignright alignjustify | ' +
            'bullist numlist outdent indent | link image | print preview media fullpage | ' +
            'forecolor backcolor emoticons | help',
        menu: {
            favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css',
        toc_depth: 3,
        toc_header: 'h3',
        quickbars_insert_toolbar: 'heading codesample quickimage quicktable | hr pagebreak',
        quickbars_selection_toolbar: 'bold italic | formatselect | quicklink blockquote h2 h3'
    });
}