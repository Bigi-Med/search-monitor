import React, { FunctionComponent } from 'react'

interface LinkBorderProps {
    link?: string;
    placeholder?: string;
    children?: React.ReactNode;
    title:string;
    onClick?: () => void
}

const LinkBorder: FunctionComponent<LinkBorderProps> = ({link, placeholder,children,title,onClick}) => {

    return (
        <div style={{
                border: '3px solid black',
                borderRadius:'20px',
                boxShadow: '10px 10px 10px 0 rgba(0, 0, 0, 0.5)',
                // background: '#0056b3',
                marginBottom:'10%',
                cursor: 'pointer',
                padding: '30px',
                color:'black'
        }} onClick={onClick}>
            <a href={link}><span style={{fontWeight:'bold', fontStyle:'italic', fontSize:'20px'}}>{title}</span><span style={{fontSize:'20px'}}>{placeholder}</span></a>
            {children}
        </div>
        );
}
export default LinkBorder