import React, { FunctionComponent } from 'react'

interface LinkBorderProps {
    link?: string;
    logo?: string;
    children?: React.ReactNode;
    onClick?: () => void
}

const LinkBorder: FunctionComponent<LinkBorderProps> = ({link, logo, children,onClick}) => {

    return (
        <div style={{
                border: '1px solid black',
                borderRadius:'20px',
                boxShadow:'0 0 10px rgba(0, 0, 0, 0.3)',
                background: '#0056b3',
                marginBottom:'10%',
                cursor: 'pointer',
                padding: '30px',
                color:'white'
        }} onClick={onClick}>
            <a href={link}>{link}</a>
            {children}
        </div>
        );
}
export default LinkBorder