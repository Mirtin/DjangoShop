const rate = (rating, post_id) => {
            fetch(`/rate/${post_id}/${rating}/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(rest => {
                window.location.reload();

            })
        }