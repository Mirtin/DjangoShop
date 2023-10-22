const rate = (rating, prod_id, user_id) => {
            fetch(`add_rating/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({"rating": rating,
                                      "prod_id": prod_id,
                                      "user_id": user_id,
                }),
            }).then(rest => {
                window.location.reload();

            })
        }