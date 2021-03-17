// https://www.youtube.com/watch?v=xq532yn8gMA


function sendRequest(url, method, data) {
    const response = axios({
        method: method,
        url: url,
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    return response
}

let products_list = [];

new Vue({
    el: '#app',
    data: {
        note: '',
        notes: [],
        product: '',
        products: [],
    },
    // функция при загрузке страницы
    created: function() {
        const vm = this;
        const r = sendRequest('/api/', 'get')
            .then(function(response) {
                vm.notes = response.data;

                try {
                    let note_name = document.getElementById('note-name').textContent;
                    for (note of vm.notes) {
                        if (note.name == note_name) {
                            vm.note = note;
                        }
                    }
                } catch (err) {
                    console.log('это точно не страница со списком продуктов');
                };

            });
    },

    methods: {
        // создание новой заметки
        createNewNote(){
            const vm = this;
            const formData = new FormData();
            formData.append('name', this.note);

            sendRequest('/api/', 'post', formData)
                .then(function(response) {
                    vm.notes.push(response.data);
                    vm.note = '';
                })
        },
        // заметка детально
        noteDetail(id) {
            // просто перенаправляем на другой url
            document.location = '/note/' + id;
        },
        // перенаправление на страницу редактирования заметки
        editNote(id) {
            document.location = '/editNote/' + id;
        },
        // удаление заметки
        deleteNote(id, index){
            const vm = this;
            sendRequest('/delete/' + id + '/', 'post')
                .then(function(response) {
                    vm.notes.splice(index, 1);
                })
        },
        // удаление продукта из заметки
        productDelete(id, index) {
            const vm = this;
            sendRequest('/delete_product/' + id + '/', 'post')
                .then(function(response) {
                    vm.note.products.splice(index, 1);
                })
        },
        // продукт куплен (completed)
        productCompleted(id, index) {
            const vm = this;

            if (vm.note.products[index].completed == false) {
                vm.note.products[index].completed = true;
                sendRequest('/completed_product/' + id + '/', 'post')
                    .then(function(response) {
                        console.log(vm.note.products[index].completed);
                    })
            } else {
                vm.note.products[index].completed = false;
                sendRequest('/not_completed_product/' + id + '/', 'post')
                    .then(function(response) {
                        console.log(vm.note.products[index].completed);
                    })
            }
        },
    }
});
