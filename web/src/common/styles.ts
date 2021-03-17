import { css } from "lit-element";

export const ColorStyles = css`
    .pf-m-success {
        color: var(--pf-global--success-color--100);
    }
    .pf-c-button.pf-m-success {
        color: var(--pf-c-button--m-primary--Color);
        background-color: var(--pf-global--success-color--100);
    }
    .pf-m-warning {
        color: var(--pf-global--warning-color--100);
    }
    .pf-c-button.pf-m-warning {
        color: var(--pf-c-button--m-primary--Color);
        background-color: var(--pf-global--warning-color--100);
    }
    .pf-m-danger {
        color: var(--pf-global--danger-color--100);
    }
    .pf-c-button.pf-m-danger {
        color: var(--pf-c-button--m-primary--Color);
        background-color: var(--pf-global--danger-color--100);
    }
`;
