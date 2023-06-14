
### standard library import
from xml.etree.ElementTree import Element


GENERAL_SURFACES_CSS = """

g.file_not_found_shapes > rect {
  fill: rgb(15, 15, 15);
  stroke: none;
}

g.file_not_found_shapes > ellipse {
  stroke: rgb(200, 0, 0);
  stroke-width: 15px;
  fill:none;
}

g.file_not_found_shapes > line {
  stroke: rgb(200, 0, 0);
  stroke-width: 15px;
}

"""


def get_not_found_surface_svg_repr(rect):

    g = Element("g", {"class": "file_not_found_shapes"})

    g.append(
        Element(
            "rect",
            {
                **{
                    attr_name: str(getattr(rect, attr_name))
                    for attr_name in ("x", "y", "width", "height")
                },
            },
        ),
    )

    ellipse_rect = rect.inflate(-16, -16)

    g.append(
        Element(
            "ellipse",
            {
                "cx": str(ellipse_rect.centerx),
                "cy": str(ellipse_rect.centery),
                "rx": str(ellipse_rect.width // 2),
                "ry": str(ellipse_rect.height // 2),
            },
        ),
    )

    slash_rect = rect.inflate(-60, -60)

    p1 = slash_rect.bottomleft
    p2 = slash_rect.topright

    g.append(
        Element(
            "line",
            {
                **{
                    key: value
                    for key, value in (
                        zip(
                            ("x1", "y1"),
                            map(str, p1),
                        )
                    )
                },
                **{
                    key: value
                    for key, value in (
                        zip(
                            ("x2", "y2"),
                            map(str, p2),
                        )
                    )
                },
            },
        ),
    )

    return g
