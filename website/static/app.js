/* Slide navbar links */

/* Clear add contacts form */

const clearAdd = () => {
  const button = document.querySelector("#add-button");

  button.onclick = (e) => {
    e.preventDefault();
    const addForm = document.querySelector("#add-contact");
    const csrf_token = document.querySelector("#csrf_token");

    contactName = addForm.name.value;
    email = addForm.email.value;
    phone = addForm.phone.value;
    Type = addForm.contact_type.value;

    fetch("/contacts", {
      method: "POST",
      body: JSON.stringify({
        csrf_token: csrf_token.value,
        name: contactName,
        email: email,
        phone: phone,
        Type: Type,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }).then(() => {
      addForm.email.value = "";
      addForm.email.value = "";
      addForm.phone.value = "";

      window.location.href = "/contacts";
    });
  };
};

const delContacts = () => {
  const delButtons = document.querySelectorAll(".deleteButton");
  for (delButton of delButtons) {
    delButton.onclick = (e) => {
      e.preventDefault();
      const contactId = e.target.dataset["id"];
      fetch(`/delete_contact/${contactId}`, {
        method: "DELETE",
      })
        .then(() => {
          window.location.href = "/contacts";
        })
        .catch((e) => {
          console.log("error", e);
        });
    };
  }
};

const cancelUpdate = () => {
  const cancelButton = document.querySelector("#cancel-button");
  cancelButton.onclick = (e) => {
    window.location.href = "/contacts";
  };
};

const app = () => {
  clearAdd();
  delContacts();
  cancelUpdate();
};

app();
