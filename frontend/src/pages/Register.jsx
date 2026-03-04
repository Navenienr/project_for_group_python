import React, { useState } from 'react'
import S from '../style/Login.module.css'
import { NavLink, useNavigate } from 'react-router-dom'

const Register = () => {
    const navigate = useNavigate();
    
    const [formData, setFormData] = useState({
        email: '',
        username: '',
        phone: '',
        password: '',
        confirmPassword: ''
    })

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }))
    }

    const handleSubmit = async (e) => {
        e.preventDefault()

        if (formData.password !== formData.confirmPassword) {
            alert("Пароли не совпадают!");
            return
        }

        try {
            console.log(formData)
            const response = await fetch('http://127.0.0.1:8000/api/core/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: formData.username,
                    email: formData.email,
                    password: formData.password,
                    password2: formData.confirmPassword,
    
                })
            })

            const data = await response.json();

            if (data.success) {
                // сохранение токена в браузере (LocalStorage)
                localStorage.setItem('userToken', data.token)
                localStorage.setItem('userName', data.user.username)
                window.dispatchEvent(new Event('authChange')) 
                // alert('Регистрация прошла успешно!')
                navigate('/')
            } else {
                const errorMsg = JSON.stringify(data.errors)
                alert('Ошибка регистрации: ' + errorMsg)
            }
        } catch (error) {
            console.error('Ошибка запроса:', error)
            alert('Не удалось связаться с сервером. Проверь, запущен ли Django.')
        }
    }

    return (
        <div className={S.container}>
            <header className={S.header}>
                <div className={S.nav_container}>
                    <NavLink to="/" className={S.logo}>
                        <span className={S.logo_icon}>🎮</span>
                        GameForum
                    </NavLink>
                </div>
            </header>
            
            <form onSubmit={handleSubmit} className={S.registration_form}>
                <div className={S.form_group}>
                    <label>Почта:</label><br />
                    <input className={S.input_field} type="email" name="email" 
                        value={formData.email} onChange={handleChange} 
                        required style={{ width: '100%', padding: '8px' }}
                    />
                </div>
          
                <div className={S.form_group}>
                    <label>Имя пользователя:</label><br />
                    <input className={S.input_field} type="text" name="username" 
                        value={formData.username} onChange={handleChange} 
                        required style={{ width: '100%', padding: '8px' }}
                    />
                </div>

                <div className={S.form_group}>
                    <label>Пароль:</label>
                    <input className={S.input_field}
                        type="password" name="password" 
                        value={formData.password} onChange={handleChange} 
                        required style={{ width: '100%', padding: '8px' }}
                    />
                </div>

                <div className={S.form_group}>
                    <label>Повторите пароль:</label>
                    <input className={S.input_field}
                        type="password" name="confirmPassword" 
                        value={formData.confirmPassword} onChange={handleChange} 
                        required style={{ width: '100%', padding: '8px' }}
                    />
                </div>
          
                <button type="submit" className={S.submit_button}>Зарегистрироваться</button>
            </form>
        </div>
    );
};

export default Register;
