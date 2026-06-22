import { patch } from "@web/core/utils/patch";
import { PosOrder } from "@point_of_sale/app/models/pos_order";

patch(PosOrder.prototype, {
    export_for_printing(baseUrl, headerData) {
        const result = super.export_for_printing(...arguments);
        const lines = this.getSortedOrderlines();
        const showReceiptImage = this.config.iface_image_receipt;
        result.orderlines = result.orderlines.map((data, index) => {
            const line = lines[index];
            if (showReceiptImage && line && line.product_id) {
                data.imageSrc = `/web/image/product.product/${line.product_id.id}/image_128`;
            } else {
                delete data.imageSrc;
            }
            return data;
        });
        return result;
    },
});
